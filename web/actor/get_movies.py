import requests
import json

TMDB_API_KEY = '9fd49ab00d660f7801565ddb3d5db886'


def get_movie_datas():
    total_data = []
    total_actor = []
    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 2):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'director': '',
                    'actors': [],
                }

                data = {
                    # "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields,
                }

                total_data.append(data)

    for data in total_data:
        movie_id = data['fields']['movie_id']

        credit_request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
        credit_info = requests.get(credit_request_url).json()
        # print(credit_request_url)
        # print(credit_info)
        # 배우는 최대 10명까지만 저장한다.
        for cast in credit_info['cast'][:10]:
            actor_field ={
                'credit_id': cast['credit_id'],
                'actor_name': cast['name'],
                'img_key': cast['profile_path']
            }
            # print(cast)
            # data['fields']['actors'].append({cast['name']:cast['profile_path']})
            data['fields']['actors'].append(cast['id'])
            actor_data = {
                'model': 'movies.actor',
                'pk': cast['id'],
                'fields': actor_field,
            }
            if actor_data not in total_actor:
                total_actor.append(actor_data)
        if credit_info['crew']:
            # data['director'] = credit_info['crew'][0]['name']
            data['fields']['director'] = credit_info['crew'][0]['name']

    for data in total_data:
        movie_id = data['fields']['movie_id']
        video_request_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&append_to_response=videos'
        # print(video_request_url)
        video_info = requests.get(video_request_url).json()
        # print(video_info['videos']['results'][0]['key'])
        data['fields']['video_key'] = video_info['videos']['results'][0]['key']

    with open("movies.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, ensure_ascii=False)


    with open("actors.json", "w", encoding="utf-8") as w:
        json.dump(total_actor, w, ensure_ascii=False)
get_movie_datas()
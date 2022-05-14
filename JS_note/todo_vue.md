state - data

getters - computed

mutations - methods => change

actions - methods => !change

---

- props는 v-for에서만 거의 사용

- input은 v-model로 엮어주는게 편함
- 이벤트리스너는 methods
- arr.splice(idx, number) : idx부터 number개 지우겠다
- if (confirm("확인?")){}
- getters는 일방적으로 받는값이라 data로 받지말고(data에서 수정하지마 state변경되면서 꼬일 수 있음) computed로 받아야함

---



- App.vue에 임포트하고 컴포넌츠 등록
- `TodoList`에서 `TodoListItem` 임포트하고 컴포넌츠 등록, 템플릿에 케밥케이스(v-for 돌리기)
  - `v-for="todo in $store.state.todos" :key="todo.date"`
  - 아니면 computed에서 todos 함수 만들어서 리턴값으로 정해주기
- `TodoForm`에서 템플릿에 input태그 만들기
-  `index.js`에서 state에 `todos`등록

- `TodoList`에 있는 todo값 prop로 내려주기
  - `:todo="todo"`

- `TodoListItem`에서 props에 type 등록, `todo.title` 출력

- `index.js`의 actions에서 `createTodo()` 함수 생성(mutations 접근)
  - `context.commit(CREATE_TODO, newTodo)`

- mutations에 `CREATE_TODO` 함수 생성
  - `state.todos.push(newTodo)`
-  -> 컴포넌트에서 액션호출해야겠지?
- `TodoForm`에서 input에서 이벤트수행했을때
  - `@keyup.enter="createTodo"`
  - 이벤트리스너는 methods
    - `createTodo () { $store.dispatch('createTodo', newTodo)}`
- data에 빈 문자열 생성 `todoTitle`
- input에 `v-model="todoTitle.trim"`
- `createTodo`에 `const newTodo`로 딕셔너리 만들어주기
  - `title, isCompleted, date`
    - date: new Date().getTime()

- `TodoListItem`에서 button 만들어주기
  - `@click="deleteTodo"` 걸어주기
- methods에 deleteTodo 함수 등록(store에 삭제 요청하기)
  - `this.$store.dispatch('deleteTodo', this.todo)`
- `index.js`의 actions에 deleteTodo 함수 등록
  - `commit('DELETE_TODO', todoItem)`
- mutations에 `DELETE_TODO(state, todoItem)` 등록
  - `const index = state.todos.indexOf(todoItem)`
  - `state.todos.splice(index, 1)`

---

### map

- TodoListItem에서 actions의 'deleteTodo' 함수를 바로 쓰고 싶다면?
  - `import { mapActions } from 'vuex'`
  - `methods: { ...mapActions(['deleteTodo']), mymethod() {} }`
  - button 에서 `@click="deleteTodo(todo)"`
    - 특수문법: deleteTodo할때 todo 꼭 넘겨주세요~

- 할일목록 클릭하면 밑줄긋기 + isCompleted 바꾸기

  - `index.js`에서 `updateTodoStatus`, `UPDATE_TODO_STATUS` 만들기

    - ```
      UPDATE_TODO_STATUS(state, todoItem) {
      state.todos = state.todos.map(todo => {
      	if (todo === todoItem){
      		todo.isComplted = !todo.isCompleted
      	} return todo
      })
      }
      ```

    - 

  - `TodoListItem`의 mapActions에 `updateTodoStatus`추가

  - 타이틀에 `@click="updateTodoStatus(todo)"`

  - `TodoListItem`에서 title에 style적용

    - `:class="{is-completed: todo.isCompleted }"`
      - 클래스바인딩 todo.isCompleted기준으로 부여
    - `text-decoration: line-through`
    - 스타일에 `scoped`써주면 현재 컴포넌트에만 적용

- 현재 전체 개수, 끝난 일 개수, 안 끝난 일 개수 구하기

  - getters에 함수 추가

    ```
    allTodosCount(state) {
    	return state.todos.length
    }
    
    completedTodos(state) {
    	return state.todos.filter(todo => {
    		return todo.isCompleted
    	}).length
    }
    
    uncompletedTodos(state) {
    	return state.todos.filter(todo => {
    		return !todo.isCompleted
    	}).length
    }
    ```

  - `App.vue`에 개수 출력

    - `import {mapGetters} from 'vuex'`

    - computed에 getters매핑

      ```
      ...mapGetters(['allTodosCount', 'completedTodos', 'uncompletedTodos'])
      ```

    - 위에서 해당 메소드변수 출력
      - `{{ allTodosCount }}`

    
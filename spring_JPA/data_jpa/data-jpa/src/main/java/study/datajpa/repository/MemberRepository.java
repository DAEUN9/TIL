package study.datajpa.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.transaction.annotation.Transactional;
import study.datajpa.entity.Member;
@Transactional
public interface MemberRepository extends JpaRepository<Member, Long> {
}

package jpabook.jpashop.domain;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter @Setter
public class Delivery {

    @Id
    @GeneratedValue
    @Column(name="delivery_id")
    private Long id;

    @OneToOne(mappedBy = "delivery")
    private Order order;

    @Embedded
    private Address address;

    // ORDINAL 절대 쓰면안됨(중간에 들어가면 오류남)
    @Enumerated(EnumType.STRING)
    private DelieryStatus status; //READY, COMP
}

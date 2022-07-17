package jpabook.jpashop;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HelloController {

    @GetMapping("hello")
    public String hello(Model model) {
        // data라는 이름의 값을 hello!!!로 넘김
        model.addAttribute("data", "hello!!!");
        //template 리턴
        return "hello";
    }
}

package com.example.zadanie3

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/api/users")
class UserController {
    private val users = listOf(
        User(1, "Jakub"),
        User(2, "Maciej"),
        User(3, "Tymoteusz")
    )

    @GetMapping
    fun getAllUsers(): List<User> = users
}

package com.example.zadanie3

import org.springframework.context.annotation.Lazy
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/auth")
class AuthController(
    @Lazy
    private val authService: AuthenticationService
) {

    @PostMapping("/login")
    fun login(@RequestBody body: LoginRequest) =
        authService.authenticate(body.username, body.password)
}

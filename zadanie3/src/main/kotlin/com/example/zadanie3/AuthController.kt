package com.example.zadanie3

import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/auth")
class AuthController(
    private val authService: AuthService
) {

    @PostMapping("/login")
    fun login(@RequestBody body: LoginRequest): AuthResult =
        authService.authenticate(body.username, body.password)
}

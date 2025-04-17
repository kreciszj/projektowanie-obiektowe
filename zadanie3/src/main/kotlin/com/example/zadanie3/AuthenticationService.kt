package com.example.zadanie3

interface AuthenticationService {
    fun authenticate(username: String, password: String): AuthResult
}

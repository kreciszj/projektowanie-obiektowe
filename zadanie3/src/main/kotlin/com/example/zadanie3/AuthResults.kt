package com.example.zadanie3

data class AuthResult(
    val success: Boolean,
    val user: User? = null,
    val token: String? = null
) {
    companion object {
        fun success(user: User, token: String) = AuthResult(true, user, token)
        fun failure() = AuthResult(false, null, null)
    }
}

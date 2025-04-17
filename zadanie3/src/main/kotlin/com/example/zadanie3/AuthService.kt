package com.example.zadanie3

import org.springframework.stereotype.Service
import java.security.MessageDigest
import java.util.UUID


@Service
class AuthService {
    private val users = mapOf(
        "alice"   to "password123".sha256(),
        "bob"     to "qwerty".sha256(),
        "charlie" to "admin!".sha256()
    )

    init {
        println(">>> AuthService eagerly initialized with ${users.size} users")
    }

    fun authenticate(username: String, password: String): AuthResult {
        val stored = users[username] ?: return AuthResult.failure()
        val ok = stored.equals(password.sha256(), true)
        return if (ok) {
            AuthResult.success(
                user  = User(id = 0, username = username),
                token = UUID.randomUUID().toString()
            )
        } else AuthResult.failure()
    }
}

data class AuthResult(
    val success: Boolean,
    val user: User? = null,
    val token: String? = null
) {
    companion object {
        fun success(user: User, token: String) = AuthResult(true, user, token)
        fun failure() = AuthResult(false)
    }
}

private fun String.sha256(): String =
    MessageDigest.getInstance("SHA-256")
        .digest(toByteArray())
        .joinToString("") { "%02x".format(it) }

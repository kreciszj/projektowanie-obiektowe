package com.example.zadanie3

import org.springframework.context.annotation.Profile
import org.springframework.stereotype.Service
import java.security.MessageDigest
import java.util.UUID

@Service
@Profile("!lazy")
class EagerAuthService : AuthenticationService {

    private val users = mapOf(
        "alice"   to "password123".sha256(),
        "bob"     to "qwerty".sha256(),
        "charlie" to "admin!".sha256()
    )

    init { println(">>> EagerAuthService initialized eagerly") }

    override fun authenticate(username: String, password: String): AuthResult {
        val stored = users[username] ?: return AuthResult.failure()
        return if (stored.equals(password.sha256(), true)) {
            AuthResult.success(User(0, username), UUID.randomUUID().toString())
        } else AuthResult.failure()
    }
}

private fun String.sha256(): String =
    MessageDigest.getInstance("SHA-256")
        .digest(toByteArray())
        .joinToString("") { "%02x".format(it) }

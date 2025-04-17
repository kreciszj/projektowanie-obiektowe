package com.example.zadanie3

import org.springframework.beans.factory.ObjectProvider
import org.springframework.boot.CommandLineRunner
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class Zadanie3Application(
	private val authServiceProvider: ObjectProvider<AuthenticationService>
) : CommandLineRunner {

	override fun run(vararg args: String?) {
		println(">>> Application started.")
	}
}

fun main(args: Array<String>) {
	runApplication<Zadanie3Application>(*args)
}

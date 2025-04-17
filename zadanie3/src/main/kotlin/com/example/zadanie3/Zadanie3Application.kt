package com.example.zadanie3

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.CommandLineRunner
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class Zadanie3Application : CommandLineRunner {
	@Autowired
	private lateinit var authService: AuthService

	override fun run(vararg args: String?) {
		println(">>> Zadanie3Application got AuthService instance: $authService")
	}
}

fun main(args: Array<String>) {
	runApplication<Zadanie3Application>(*args)
}

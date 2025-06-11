package com.example.zadanie9

import io.realm.kotlin.Realm
import io.realm.kotlin.RealmConfiguration
import io.realm.kotlin.ext.query

object RealmDB {

    val realm: Realm by lazy {
        val config = RealmConfiguration.Builder(
            schema = setOf(CartItem::class)
        ).build()
        Realm.open(config)
    }

    fun addToCart(product: Product) {
        realm.writeBlocking {
            copyToRealm(
                CartItem().apply {
                    productId = product.id
                    name = product.name
                }
            )
        }
    }

    fun getCartItems(): List<CartItem> =
        realm.query<CartItem>().find()
}

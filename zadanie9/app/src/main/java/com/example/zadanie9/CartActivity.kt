package com.example.zadanie9

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.sp

class CartActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        title = "Cart"
        val cartItems = RealmDB.getCartItems()
        setContent {
            MaterialTheme {
                Surface(modifier = Modifier.fillMaxSize()) {
                    LazyColumn {
                        if (cartItems.isEmpty()) {
                            item { Text(text = "Cart is empty", fontSize = 20.sp) }
                        } else {
                            items(cartItems) { item ->
                                Text(text = item.name, fontSize = 20.sp)
                            }
                        }
                    }
                }
            }
        }
    }
}

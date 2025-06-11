package com.example.zadanie9

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.FloatingActionButton
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ShoppingCart

class ProductActivity : ComponentActivity() {

    private val products = listOf(
        Product(1, 1, "Water"),
        Product(2, 1, "Coffee"),
        Product(3, 2, "Chips"),
        Product(4, 2, "Cookies"),
        Product(5, 3, "Apple"),
        Product(6, 3, "Banana")
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val id = intent.getIntExtra("catId", 0)
        val list = products.filter { it.categoryId == id }
        title = intent.getStringExtra("catName") ?: "Products"
        setContent {
            MaterialTheme {
                Surface(modifier = Modifier.fillMaxSize()) {
                    ProductScreen(
                        products = list,
                        onAdd = { Cart.items.add(it) },
                        onOpenCart = { startActivity(Intent(this, CartActivity::class.java)) }
                    )
                }
            }
        }
    }
}

@Composable
fun ProductScreen(
    products: List<Product>,
    onAdd: (Product) -> Unit,
    onOpenCart: () -> Unit
) {
    androidx.compose.material3.Scaffold(
        floatingActionButton = {
            FloatingActionButton(onClick = onOpenCart) {
                Icon(Icons.Filled.ShoppingCart, contentDescription = null)
            }
        }
    ) { pad ->
        LazyColumn(modifier = Modifier.padding(pad)) {
            items(products) { item ->
                Text(
                    text = item.name,
                    fontSize = 20.sp,
                    modifier = Modifier
                        .fillMaxSize()
                        .clickable { onAdd(item) }
                        .padding(8.dp)
                )
            }
        }
    }
}

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
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ShoppingCart
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.sp

class MainActivity : ComponentActivity() {

    private val categories = listOf(
        Category(1, "Drinks"),
        Category(2, "Snacks"),
        Category(3, "Fruit")
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                Surface(modifier = Modifier.fillMaxSize()) {
                    CategoryScreen(
                        categories = categories,
                        onSelect = { category ->
                            startActivity(
                                Intent(this, ProductActivity::class.java)
                                    .putExtra("catId", category.id)
                                    .putExtra("catName", category.name)
                            )
                        },
                        onOpenCart = {
                            startActivity(Intent(this, CartActivity::class.java))
                        }
                    )
                }
            }
        }
    }
}

@Composable
fun CategoryList(
    list: List<Category>,
    onClick: (Category) -> Unit,
    modifier: Modifier = Modifier
) {
    LazyColumn(modifier = modifier) {
        items(list) { item ->
            Text(
                text = item.name,
                fontSize = 24.sp,
                modifier = Modifier
                    .clickable { onClick(item) }
                    .fillMaxSize()
            )
        }
    }
}

@Composable
fun CategoryScreen(
    categories: List<Category>,
    onSelect: (Category) -> Unit,
    onOpenCart: () -> Unit
) {
    Scaffold(
        floatingActionButton = {
            FloatingActionButton(onClick = onOpenCart) {
                Icon(Icons.Filled.ShoppingCart, contentDescription = null)
            }
        }
    ) { pad ->
        CategoryList(
            list = categories,
            onClick = onSelect,
            modifier = Modifier.padding(pad)
        )
    }
}

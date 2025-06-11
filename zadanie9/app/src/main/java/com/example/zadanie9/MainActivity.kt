package com.example.zadanie9

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
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
                    CategoryList(categories) { category ->
                        startActivity(
                            Intent(this, ProductActivity::class.java)
                                .putExtra("catId", category.id)
                                .putExtra("catName", category.name)
                        )
                    }
                }
            }
        }
    }
}

@Composable
fun CategoryList(list: List<Category>, onClick: (Category) -> Unit) {
    LazyColumn {
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

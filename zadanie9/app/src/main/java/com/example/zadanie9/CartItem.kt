package com.example.zadanie9

import io.realm.kotlin.types.RealmObject
import io.realm.kotlin.types.annotations.PrimaryKey
import org.mongodb.kbson.ObjectId

class CartItem : RealmObject {
    @PrimaryKey
    var _id: ObjectId = ObjectId()
    var productId: Int = 0
    var name: String = ""
}

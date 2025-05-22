import Fluent
import Vapor

final class Product: Model, @unchecked Sendable, Content {
    static let schema = "products"

    @ID(key: .id) var id: UUID?
    @Field(key: "name") var name: String
    @OptionalField(key: "description") var description: String?
    @Field(key: "price") var price: Double

    init() { }

    init(id: UUID? = nil, name: String, description: String? = nil, price: Double) {
        self.id = id
        self.name = name
        self.description = description
        self.price = price
    }
}

import Fluent

struct CreateProduct: AsyncMigration {
    func prepare(on db: any Database) async throws {
        try await db.schema(Product.schema)
            .id()
            .field("name", .string, .required)
            .field("description", .string)
            .field("price", .double, .required)
            .create()
    }
    func revert(on db: any Database) async throws {
        try await db.schema(Product.schema).delete()
    }
}

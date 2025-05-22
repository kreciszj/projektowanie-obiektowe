import Fluent
import Vapor

struct ProductController: RouteCollection {
    func boot(routes: any RoutesBuilder) throws {
        let products = routes.grouped("products")
        products.get(use: index)
        products.post(use: create)
        products.group(":productID") { product in
            product.get(use: show)
            product.put(use: update)
            product.delete(use: delete)
        }
    }

    // GET /products
    func index(req: Request) async throws -> [Product] {
        try await Product.query(on: req.db).all()
    }

    // POST /products
    func create(req: Request) async throws -> Product {
        let product = try req.content.decode(Product.self)
        try await product.save(on: req.db)
        return product
    }

    // GET /products/:productID
    func show(req: Request) async throws -> Product {
        guard let product = try await Product.find(req.parameters.get("productID"), on: req.db) else {
            throw Abort(.notFound)
        }
        return product
    }

    // PUT /products/:productID
    func update(req: Request) async throws -> Product {
        let input = try req.content.decode(Product.self)

        guard let product = try await Product.find(req.parameters.get("productID"), on: req.db) else {
            throw Abort(.notFound)
        }
        product.name = input.name
        product.description = input.description
        product.price = input.price

        try await product.update(on: req.db)
        return product
    }

    // DELETE /products/:productID
    func delete(req: Request) async throws -> HTTPStatus {
        guard let product = try await Product.find(req.parameters.get("productID"), on: req.db) else {
            throw Abort(.notFound)
        }
        try await product.delete(on: req.db)
        return .noContent
    }
}

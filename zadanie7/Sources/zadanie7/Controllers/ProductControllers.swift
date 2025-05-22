import Vapor        
import Fluent
import Leaf

struct ProductController: RouteCollection {

    // MARK: - Rejestr tras
    func boot(routes: any RoutesBuilder) throws {
        let products = routes.grouped("products")

        // ---- JSON API (z oceny 3.0) ----
        products.get(use: apiIndex)          // GET /products
        products.post(use: apiCreate)        // POST /products
        products.group(":productID") { item in
            item.get(use: apiShow)           // GET /products/:id
            item.put(use: apiUpdate)         // PUT /products/:id
            item.delete(use: apiDelete)      // DELETE /products/:id
        }

        // ---- Widoki HTML (3.5) ----
        products.get("list", use: listView)               // /products/list
        products.get("new", use: createView)              // formularz
        products.post("new", use: createHTML)             // zapis POST
        products.get(":productID", use: detailView)       // /products/:id
        products.get(":productID", "edit", use: editView) // /products/:id/edit (GET)
        products.post(":productID", "edit", use: updateHTML)   // (POST)
        products.post(":productID", "delete", use: deleteHTML) // (POST)
    }

    // MARK: - JSON handlers
    func apiIndex(req: Request) async throws -> [Product] {
        try await Product.query(on: req.db).all()
    }

    func apiCreate(req: Request) async throws -> Product {
        let product = try req.content.decode(Product.self)
        try await product.save(on: req.db)
        return product
    }

    func apiShow(req: Request) async throws -> Product {
        guard let p = try await Product.find(req.parameters.get("productID"), on: req.db)
        else { throw Abort(.notFound) }
        return p
    }

    func apiUpdate(req: Request) async throws -> Product {
        let input = try req.content.decode(Product.self)
        guard let p = try await Product.find(req.parameters.get("productID"), on: req.db)
        else { throw Abort(.notFound) }
        p.name = input.name; p.description = input.description; p.price = input.price
        try await p.update(on: req.db)
        return p
    }

    func apiDelete(req: Request) async throws -> HTTPStatus {
        guard let p = try await Product.find(req.parameters.get("productID"), on: req.db)
        else { throw Abort(.notFound) }
        try await p.delete(on: req.db)
        return .noContent
    }

    // MARK: - Widoki HTML
    func listView(req: Request) async throws -> View {
        let items = try await Product.query(on: req.db).all()
        struct Ctx: Content { let products: [Product] }
        return try await req.view.render("products", Ctx(products: items))
    }

    func createView(req: Request) async throws -> View {
        try await req.view.render("productCreate")
    }

    func detailView(req: Request) async throws -> View {
        guard let p = try await Product.find(req.parameters.get("productID"), on: req.db)
        else { throw Abort(.notFound) }
        return try await req.view.render("product", p)
    }

    func editView(req: Request) async throws -> View {
        guard let p = try await Product.find(req.parameters.get("productID"), on: req.db)
        else { throw Abort(.notFound) }
        return try await req.view.render("productEdit", p)
    }

    // --- obsługa formularzy POST ---
    func createHTML(req: Request) async throws -> Response {
        let product = try req.content.decode(Product.self)
        try await product.save(on: req.db)
        return req.redirect(to: "/products/list")
    }

    func updateHTML(req: Request) async throws -> Response {
        guard let p = try await Product.find(req.parameters.get("productID"), on: req.db)
        else { throw Abort(.notFound) }
        let input = try req.content.decode(Product.self)
        p.name = input.name; p.description = input.description; p.price = input.price
        try await p.update(on: req.db)
        return req.redirect(to: "/products/list")
    }

    func deleteHTML(req: Request) async throws -> Response {
        guard let p = try await Product.find(req.parameters.get("productID"), on: req.db)
        else { throw Abort(.notFound) }
        try await p.delete(on: req.db)
        return req.redirect(to: "/products/list")
    }
}

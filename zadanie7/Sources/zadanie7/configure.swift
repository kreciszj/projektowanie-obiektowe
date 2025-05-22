import NIOSSL
import Fluent
import FluentSQLiteDriver
import Vapor
import Leaf

public func configure(_ app: Application) async throws {
    app.views.use(.leaf)
    app.databases.use(.sqlite(.file("db.sqlite")), as: .sqlite)

    app.migrations.add(CreateProduct())
    app.middleware.use(FileMiddleware(publicDirectory: app.directory.publicDirectory))

    if app.environment == .development {
        try await app.autoMigrate()
    }

    try routes(app)
}

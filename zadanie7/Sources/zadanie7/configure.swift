import NIOSSL
import Fluent
import FluentSQLiteDriver
import Vapor

// configures your application
public func configure(_ app: Application) async throws {
    // SQLite db.sqlite w folderze projektu
    app.databases.use(.sqlite(.file("db.sqlite")), as: .sqlite)

    // Rejestruj migracje
    app.migrations.add(CreateProduct())

    // (opcjonalnie) auto-migrate przy każdym starcie w trybie dev
    if app.environment == .development {
        try await app.autoMigrate()
    }

    // register routes
    try routes(app)
}

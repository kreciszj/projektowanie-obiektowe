<?php

namespace App\Controller;

use App\Entity\Product;
use Doctrine\Persistence\ManagerRegistry;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/product')]
class ProductController extends AbstractController
{
    /**
     * READ (list all products)
     */
    #[Route('/', name: 'product_index', methods: ['GET'])]
    public function index(ManagerRegistry $doctrine): JsonResponse
    {
        $products = $doctrine->getRepository(Product::class)->findAll();

        $data = [];
        foreach ($products as $product) {
            $data[] = [
                'id'         => $product->getId(),
                'name'       => $product->getName(),
                'price'      => $product->getPrice(),
                'description'=> $product->getDescription(),
                'createdAt'  => $product->getCreatedAt()->format('Y-m-d H:i:s'),
            ];
        }

        return $this->json($data);
    }

    /**
     * CREATE (create a new product)
     */
    #[Route('/create', name: 'product_create', methods: ['POST'])]
    public function create(Request $request, ManagerRegistry $doctrine): JsonResponse
    {
        $data = json_decode($request->getContent(), true);

        $name        = $data['name']        ?? null;
        $price       = $data['price']       ?? null;
        $description = $data['description'] ?? null;

        if (!$name || !$price || !$description) {
            return $this->json(['error' => 'Missing required fields'], 400);
        }

        $product = new Product();
        $product->setName($name);
        $product->setPrice((float)$price);
        $product->setDescription($description);
        $product->setCreatedAt(new \DateTime());

        $entityManager = $doctrine->getManager();
        $entityManager->persist($product);
        $entityManager->flush();

        return $this->json([
            'message' => 'Product created successfully',
            'id'      => $product->getId(),
        ]);
    }

    /**
     * UPDATE (update a product)
     */
    #[Route('/{id}', name: 'product_update', methods: ['PUT', 'PATCH'])]
    public function update(int $id, Request $request, ManagerRegistry $doctrine): JsonResponse
    {
        $entityManager = $doctrine->getManager();
        $product = $entityManager->getRepository(Product::class)->find($id);

        if (!$product) {
            return $this->json(['error' => 'Product not found'], 404);
        }

        $data = json_decode($request->getContent(), true);

        // Jeśli klucza nie ma w tablicy, użyj aktualnej wartości
        $name        = $data['name']        ?? $product->getName();
        $price       = $data['price']       ?? $product->getPrice();
        $description = $data['description'] ?? $product->getDescription();

        $product->setName($name);
        $product->setPrice((float)$price);
        $product->setDescription($description);

        $entityManager->flush();

        return $this->json([
            'message' => 'Product updated successfully',
            'id'      => $product->getId(),
        ]);
    }

    /**
     * DELETE (delete a product)
     */
    #[Route('/{id}', name: 'product_delete', methods: ['DELETE'])]
    public function delete(int $id, ManagerRegistry $doctrine): JsonResponse
    {
        $entityManager = $doctrine->getManager();
        $product = $entityManager->getRepository(Product::class)->find($id);

        if (!$product) {
            return $this->json(['error' => 'Product not found'], 404);
        }

        $entityManager->remove($product);
        $entityManager->flush();

        return $this->json(['message' => 'Product deleted successfully']);
    }
}

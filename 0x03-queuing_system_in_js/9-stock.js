import express from "express";
import { createClient } from "redis";
import { promisify } from "util";

const app = express();
const port = 1245;

const client = createClient();

const getAsync = promisify(client.get).bind(client);

const listProducts = [
    {
        itemId: 1,
        itemName: "Suitcase 250",
        price: 50,
        initialAvailableQuantity: 4,
    },
    {
        itemId: 2,
        itemName: "Suitcase 450",
        price: 100,
        initialAvailableQuantity: 10,
    },
    {
        itemId: 3,
        itemName: "Suitcase 650",
        price: 350,
        initialAvailableQuantity: 2,
    },
    {
        itemId: 4,
        itemName: "Suitcase 1050",
        price: 550,
        initialAvailableQuantity: 5,
    },
];

app.get("/list_products", (_req, res) => {
    res.json(listProducts);
});

app.get("/list_products/:itemId", async (req, res) => {
    const { itemId } = req.params;
    const product = listProducts.find(
        (item) => item.itemId === parseInt(itemId)
    );
    if (!product) {
        res.json({ status: "Product not found" });
    } else {
        const currentQuantity = await getCurrentReservedStockById(itemId);
        res.json({ ...product, currentQuantity });
    }
});

app.get("/reserve_product/:itemId", async (req, res) => {
    const { itemId } = req.params;
    const product = listProducts.find(
        (item) => item.itemId === parseInt(itemId)
    );
    if (!product) {
        res.json({ status: "Product not found" });
    } else {
        const currentQuantity = await getCurrentReservedStockById(itemId);
        if (currentQuantity <= 0) {
            res.json({
                status: "Not enough stock available",
                itemId: parseInt(itemId),
            });
        } else {
            await reserveStockById(itemId, currentQuantity - 1);
            res.json({
                status: "Reservation confirmed",
                itemId: parseInt(itemId),
            });
        }
    }
});
async function reserveStockById(itemId, stock) {
    await client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
    const reservedStock = await getAsync(`item.${itemId}`);
    return parseInt(reservedStock) || 0;
}
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

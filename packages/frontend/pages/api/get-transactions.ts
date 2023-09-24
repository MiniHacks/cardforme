import { plaidClient } from "../../lib/plaid";

export default async function handler(req, res) {
  try {
    // Calculate the start date for two years ago
    const currentDate = new Date();
    const twoYearsAgo = new Date(currentDate);
    twoYearsAgo.setFullYear(currentDate.getFullYear() - 2);

    // Format the dates as ISO strings (YYYY-MM-DD)
    const startDate = twoYearsAgo.toISOString().split("T")[0];
    const endDate = currentDate.toISOString().split("T")[0];

    // Retrieve the access token from the session
    const access_token = req.headers.authorization;
    if (!access_token) {
      return res
        .status(401)
        .json({ error: "Access token not found in session" });
    }

    // Make a request to Plaid to fetch transaction data using the access token
    const transactionsResponse = await plaidClient.transactionsGet({
      access_token,
      start_date: startDate, // Use the calculated start date
      end_date: endDate, // Use the current date as the end date
      // Add any other required parameters as needed
    });

    // Handle the response from Plaid and send it as JSON
    return res.json(transactionsResponse.data);
  } catch (error) {
    console.error("Error fetching transactions:", error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
}

// access_token:access-sandbox-f3d77646-129d-49ff-9de3-a432927df29f

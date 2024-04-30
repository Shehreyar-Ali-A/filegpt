import { NextRequest } from "next/server";
import { getChatFromUserId } from "../../../../lib/AxiosRequests"

export async function GET(req: NextRequest) {
    const arr = req.url!.split("/")
    const userId = arr[arr.length - 1]
    const response: any = await getChatFromUserId(userId)

    return new Response(JSON.stringify(response), { status: 200});
}
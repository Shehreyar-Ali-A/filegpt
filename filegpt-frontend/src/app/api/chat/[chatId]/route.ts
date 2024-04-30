import { NextRequest } from "next/server";
import { getMessagesFromChatId } from "../../../../lib/AxiosRequests"

export async function GET(req: NextRequest) {
    const arr = req.url!.split("/")
    const chatId = arr[arr.length - 1]
    const response: any = await getMessagesFromChatId(parseInt(chatId))

    return new Response(JSON.stringify(response), { status: 200});
}
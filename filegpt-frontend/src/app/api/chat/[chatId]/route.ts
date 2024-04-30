import { getMessagesFromChatId } from "../../../../lib/AxiosRequests"
import { NextApiRequest, NextApiResponse } from 'next';

export async function GET(req: NextApiRequest) {
    const arr = req.url!.split("/")
    const chatId = arr[arr.length - 1]
    const response: any = await getMessagesFromChatId(parseInt(chatId))

    return new Response(JSON.stringify(response), { status: 200});
}
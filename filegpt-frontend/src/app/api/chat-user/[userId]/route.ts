import { getChatFromUserId } from "../../../../lib/AxiosRequests"
import { NextApiRequest } from 'next';

export async function GET(req: NextApiRequest) {
    const arr = req.url!.split("/")
    const userId = arr[arr.length - 1]
    const response: any = await getChatFromUserId(userId)

    return new Response(JSON.stringify(response), { status: 200});
}
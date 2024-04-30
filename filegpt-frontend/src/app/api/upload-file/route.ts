
import { uploadFile } from "../../../lib/AxiosRequests"

export async function POST(req: Request) {

    const formData = await req.formData()
    const response = await uploadFile(formData)
    return new Response(JSON.stringify(response), { status: 200 });
}

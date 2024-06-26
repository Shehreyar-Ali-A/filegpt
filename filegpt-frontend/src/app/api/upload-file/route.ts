
import { NextRequest } from "next/server";
import { uploadFile } from "../../../lib/AxiosRequests"
import cors from 'cors'


export async function POST(req: NextRequest) {

    const formData = await req.formData()
    const response = await uploadFile(formData)
    return new Response(JSON.stringify(response), { status: 201 });

}

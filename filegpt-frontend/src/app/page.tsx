import { Button } from "@/components/ui/button";
import { UserButton } from "@clerk/nextjs";
import { auth } from "@clerk/nextjs/server"
import Link from "next/link";
import { ArrowRight, LogIn } from "lucide-react";
import FileUpload from "@/components/FileUpload";
import axios from "axios";
import React from "react";

export default async function Home() {
  const { userId } = await auth();
  const isAuth = !!userId;

  let firstChat: any;

  if (userId) {
    const res = await axios.get(`http://localhost:3030/api/chat-user/${userId}`);
    if (res.data) {
      firstChat = res.data[0];
    }
  }

  return (
    <div className="w-screen min-h-screen bg-gradient-to-r from-indigo-200 via-red-200 to-yellow-100">
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
        <div className="flex flex-col items-center text-center">
          <div className="flex items-center">
            <h1 className="mr-3 text-5xl font-semibold">Chat with any PDF/Image</h1>
            <UserButton afterSignOutUrl="/" />
          </div>

          <div className="flex mt-2">
            {isAuth && firstChat && (
              <>
                <Link href={`/chat/${firstChat.id}`}>
                  <Button>
                    Go to Chats <ArrowRight className="ml-2" />
                  </Button>
                </Link>
                {/* <div className="ml-3">
                  <SubscriptionButton isPro={isPro} />
                </div> */}
              </>
            )}
          </div>

          <p className="max-w-xl mt-1 text-lg text-slate-600">
            Upload a .pdf or image file (.jpeg, .jpg, .png) and ask FileGPT any questions about them!
          </p>

          <div className="w-full mt-4">
            {isAuth ? (
              <FileUpload user_id={userId}/>
              // <div>File upload</div>
            ) : (
              <Link href="/sign-in">
                <Button>
                  Login to get Started!
                  <LogIn className="w-4 h-4 ml-2" />
                </Button>
              </Link>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

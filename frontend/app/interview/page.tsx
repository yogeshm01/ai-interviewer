"use client";

import { useSearchParams } from "next/navigation";

import ChatBox from "@/components/ChatBox";

export default function InterviewPage() {

    const searchParams =
        useSearchParams();

    const resumeId =
        searchParams.get("resume_id");

    if (!resumeId) {

        return (
            <main className="min-h-screen bg-black text-white flex items-center justify-center">
                Missing Resume ID
            </main>
        );
    }

    return (
        <main className="min-h-screen bg-black text-white">

            <ChatBox resumeId={resumeId} />

        </main>
    );
}
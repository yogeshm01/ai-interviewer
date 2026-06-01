"use client";

import { useSearchParams } from "next/navigation";
import { Suspense } from "react";

import ChatBox from "@/components/ChatBox";

function InterviewContent() {
    const searchParams = useSearchParams();
    const resumeId = searchParams.get("resume_id");

    if (!resumeId) {
        return (
            <div className="min-h-screen bg-black text-white flex items-center justify-center">
                Missing Resume ID
            </div>
        );
    }

    return <ChatBox resumeId={resumeId} />;
}

export default function InterviewPage() {
    return (
        <main className="min-h-screen bg-black text-white">
            <Suspense fallback={
                <div className="min-h-screen bg-black text-white flex items-center justify-center text-lg">
                    Loading Interview...
                </div>
            }>
                <InterviewContent />
            </Suspense>
        </main>
    );
}
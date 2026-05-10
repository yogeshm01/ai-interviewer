"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import API from "@/services/api";

import MessageBubble from "./MessageBubble";

type Message = {
    role: "ai" | "user";
    message: string;
};

type Props = {
    resumeId: string;
};

export default function ChatBox({
    resumeId,
}: Props) {

    const [messages, setMessages] =
        useState<Message[]>([]);

    const [input, setInput] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const router = useRouter();


    // Start interview automatically
    useEffect(() => {
        const startInterview = async () => {
            try {
                setLoading(true);
                const response = await API.get(
                    `/start-interview/${resumeId}`
                );
                const firstQuestion =
                    response.data.question;
                setMessages([
                    {
                        role: "ai",
                        message: firstQuestion,
                    },
                ]);

            } catch (error) {

                console.error(error);

            } finally {

                setLoading(false);
            }
        };

        startInterview();

    }, [resumeId]);

    const sendAnswer = async () => {
        if (!input.trim()) return;
        const userAnswer = input;
        // Add user message
        setMessages((prev) => [
            ...prev,
            {
                role: "user",
                message: userAnswer,
            },
        ]);
        setInput("");

        try {

            setLoading(true);

            const response = await API.post(
                `/submit-answer/${resumeId}`,
                {
                    answer: userAnswer,
                }
            );

            // Interview finished
            if (response.data.final_report) {

                const reportData =
                    encodeURIComponent(
                        JSON.stringify(
                            response.data.final_report
                        )
                    );

                router.push(
                    `/report?data=${reportData}`
                );

                return;
            }

            const nextQuestion =
                response.data.next_question;

            // Add AI response
            setMessages((prev) => [
                ...prev,
                {
                    role: "ai",
                    message: nextQuestion,
                },
            ]);

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);
        }
    };

    return (
        <div className="flex flex-col h-screen max-w-5xl mx-auto">

            {/* Header */}
            <div className="border-b border-zinc-800 px-6 py-5">

                <h1 className="text-xl font-semibold">
                    AI Interview Session
                </h1>

            </div>

            {/* Messages */}
            <div className="flex-1 overflow-y-auto px-6 py-8 space-y-6">

                {messages.map((msg, index) => (

                    <MessageBubble
                        key={index}
                        role={msg.role}
                        message={msg.message}
                    />
                ))}

                {loading && (
                    <div className="text-gray-500 text-sm">
                        AI is thinking...
                    </div>
                )}

            </div>

            {/* Input Area */}
            <div className="border-t border-zinc-800 p-6 flex gap-4">

                <textarea
                    value={input}
                    onChange={(e) =>
                        setInput(e.target.value)
                    }
                    placeholder="Type your answer..."
                    rows={3}
                    className="flex-1 bg-zinc-900 border border-zinc-800 rounded-xl p-4 text-white resize-none outline-none"
                />

                <button
                    onClick={sendAnswer}
                    disabled={loading}
                    className="bg-white text-black px-6 rounded-xl font-semibold hover:opacity-80 transition disabled:opacity-50"
                >
                    Send
                </button>

            </div>

        </div>
    );
}
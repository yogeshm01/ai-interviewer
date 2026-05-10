type Props = {
    role: "ai" | "user";
    message: string;
};

export default function MessageBubble({
    role,
    message,
}: Props) {

    const isAI = role === "ai";

    return (
        <div
            className={`flex ${isAI
                    ? "justify-start"
                    : "justify-end"
                }`}
        >
            <div
                className={`max-w-2xl px-5 py-4 rounded-2xl text-sm leading-relaxed ${isAI
                        ? "bg-zinc-900 border border-zinc-800 text-white"
                        : "bg-white text-black"
                    }`}
            >
                {message}
            </div>
        </div>
    );
}
import Link from "next/link";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-black text-white flex flex-col items-center justify-center px-6">

      <div className="max-w-4xl text-center">

        <h1 className="text-6xl font-bold leading-tight">
          Agentic AI Interview Copilot
        </h1>

        <p className="text-gray-400 mt-6 text-xl">
          Resume-aware adaptive mock interviews powered by
          multi-agent AI workflows.
        </p>

        <div className="mt-10">
          <Link
            href="/upload"
            className="bg-white text-black px-8 py-4 rounded-xl text-lg font-semibold hover:opacity-80 transition"
          >
            Start Interview
          </Link>
        </div>

      </div>

    </main>
  );
}
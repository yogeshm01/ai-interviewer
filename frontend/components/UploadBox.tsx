"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import API from "@/services/api";

export default function UploadBox() {

    const router = useRouter();

    const [file, setFile] = useState<File | null>(null);

    const [loading, setLoading] = useState(false);

    const handleUpload = async () => {

        if (!file) {

            alert("Please select a PDF resume.");

            return;
        }

        try {

            setLoading(true);

            const formData = new FormData();

            formData.append("file", file);

            const response = await API.post(
                "/upload-resume",
                formData,
                {
                    headers: {
                        "Content-Type":
                            "multipart/form-data",
                    },
                }
            );

            const resumeId =
                response.data.resume_id;

            router.push(
                `/interview?resume_id=${resumeId}`
            );

        } catch (error) {

            console.error(error);

            alert("Resume upload failed.");

        } finally {

            setLoading(false);
        }
    };

    return (
        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-10 w-full max-w-2xl">

            <h2 className="text-3xl font-bold text-white mb-3">
                Upload Your Resume
            </h2>

            <p className="text-gray-400 mb-8">
                Upload your PDF resume to begin
                your personalized AI interview.
            </p>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) => {

                    if (e.target.files?.[0]) {

                        setFile(e.target.files[0]);
                    }
                }}
                className="w-full bg-black border border-zinc-700 rounded-xl p-4 text-gray-300"
            />

            <button
                onClick={handleUpload}
                disabled={loading}
                className="mt-6 w-full bg-white text-black py-4 rounded-xl font-semibold hover:opacity-80 transition disabled:opacity-50"
            >
                {loading
                    ? "Uploading Resume..."
                    : "Start AI Interview"}
            </button>

        </div>
    );
}
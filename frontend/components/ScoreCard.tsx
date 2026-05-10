type Props = {
    title: string;
    items: string[];
};

export default function ScoreCard({
    title,
    items,
}: Props) {

    return (
        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

            <h2 className="text-xl font-semibold mb-4">
                {title}
            </h2>

            <ul className="space-y-3">

                {items.map((item, index) => (

                    <li
                        key={index}
                        className="text-gray-300"
                    >
                        • {item}
                    </li>
                ))}

            </ul>

        </div>
    );
}
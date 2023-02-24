function Lessons({title, content, page_number, page_total, page_setter}: {title: string, content: JSX.Element, page_number: number, page_total: number, page_setter: React.Dispatch<React.SetStateAction<number>>}) {
    return (
        <div className="flex flex-col h-full">
            <div>
                <h2 className="m-4 text-4xl font-extrabold leading-none tracking-tight md:text-5xl lg:text-6xl text-white">{title}</h2>
            </div>
            <div className="grow">
                {content}
            </div>
            <div className="p-4 btn-group flex justify-center">
                <button className="btn" onClick={() => page_setter((page_number) => change_page_handler(page_number, page_total, -1))}>«</button>
                <button className="btn">Page {page_number}</button>
                <button className="btn" onClick={() => page_setter((page_number) => change_page_handler(page_number, page_total, +1))}>»</button>
            </div>
        </div>
    )
}

function change_page_handler(page_number: number, page_total: number, next: number ): number {
    if (page_number + next < 1) {
        return 1
    }
    if (page_number + next > page_total) {
        return page_total
    }

    return page_number + next
}

export default Lessons;
import Lessons from "../../../components/lessons";
import HomeButton from "../../../components/homeButton";
import { useState } from "react";

function Exemple() {
    const [page, setPage] = useState(1);
    const pages_content = [
        content_page_1,
        content_page_2,
        content_page_3,
        content_page_4,
        content_page_5,
    ];

    return (
        <div className="h-[94vh]">
            <HomeButton />
            <Lessons title={"title"} content={pages_content[page - 1]()} page_number={page} page_total={5} page_setter={setPage} />
        </div>
    );
}

function content_page_1() {
    return (
        <div>
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 p-4">
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae, animi eaque tenetur nam illum soluta nihil dolores laudantium necessitatibus ex voluptatum ad hic odit, veniam optio in quos incidunt quidem!</p>
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur perspiciatis sapiente accusamus et aliquid eveniet dolorum assumenda atque recusandae eum maiores qui nobis quia ipsam eos suscipit voluptas, nesciunt ex?</p>
            </div>
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 p-4">
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae, animi eaque tenetur nam illum soluta nihil dolores laudantium necessitatibus ex voluptatum ad hic odit, veniam optio in quos incidunt quidem!</p>
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur perspiciatis sapiente accusamus et aliquid eveniet dolorum assumenda atque recusandae eum maiores qui nobis quia ipsam eos suscipit voluptas, nesciunt ex?</p>
            </div>
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 p-4">
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae, animi eaque tenetur nam illum soluta nihil dolores laudantium necessitatibus ex voluptatum ad hic odit, veniam optio in quos incidunt quidem!</p>
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur perspiciatis sapiente accusamus et aliquid eveniet dolorum assumenda atque recusandae eum maiores qui nobis quia ipsam eos suscipit voluptas, nesciunt ex?</p>
            </div>
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 p-4">
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae, animi eaque tenetur nam illum soluta nihil dolores laudantium necessitatibus ex voluptatum ad hic odit, veniam optio in quos incidunt quidem!</p>
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur perspiciatis sapiente accusamus et aliquid eveniet dolorum assumenda atque recusandae eum maiores qui nobis quia ipsam eos suscipit voluptas, nesciunt ex?</p>
            </div>
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 p-4">
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae, animi eaque tenetur nam illum soluta nihil dolores laudantium necessitatibus ex voluptatum ad hic odit, veniam optio in quos incidunt quidem!</p>
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur perspiciatis sapiente accusamus et aliquid eveniet dolorum assumenda atque recusandae eum maiores qui nobis quia ipsam eos suscipit voluptas, nesciunt ex?</p>
            </div>
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 p-4">
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae, animi eaque tenetur nam illum soluta nihil dolores laudantium necessitatibus ex voluptatum ad hic odit, veniam optio in quos incidunt quidem!</p>
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur perspiciatis sapiente accusamus et aliquid eveniet dolorum assumenda atque recusandae eum maiores qui nobis quia ipsam eos suscipit voluptas, nesciunt ex?</p>
            </div>
        </div>
    );
}

function content_page_2() {
    return (
        <div>
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 p-4">
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae, animi eaque tenetur nam illum soluta nihil dolores laudantium necessitatibus ex voluptatum ad hic odit, veniam optio in quos incidunt quidem!</p>
                <p className="mb-3 font-normal text-gray-200">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur perspiciatis sapiente accusamus et aliquid eveniet dolorum assumenda atque recusandae eum maiores qui nobis quia ipsam eos suscipit voluptas, nesciunt ex?</p>
            </div>
        </div>
    )
}

function content_page_3() {
    return (
        <div>
            <p>Empty content page 3</p>
        </div>
    )
}

function content_page_4() {
    return (
        <div>
            <p>Empty content page 4</p>
        </div>
    )
}

function content_page_5() {
    return (
        <div>
            <p>Empty content page 5</p>
        </div>
    )
}

export default Exemple;
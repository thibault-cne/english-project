import { useState } from "react";

type Questionaire = {
    question: string,
    options: [string, string, string, string],
    answer: number,
    question_number: number,
    question_total: number,
    question_setter: React.Dispatch<React.SetStateAction<number>>
}

function Questionaire({question, options, answer, question_number, question_total, question_setter}: Questionaire) {
    const [state, set_state] = useState(["", "", "", ""]);
    
    return (
        <div className="container">
            <div className="flex justify-end">
                <span>{question_number + 1} / {question_total}</span>
            </div>
            <div className="bg-white rounded-sm p-4 text-center mt-4">
                <h2 className="text-slate-800 text-2xl font-light">{question}</h2>
            </div>
            <div className="flex flex-col grow mt-4">
                <div className="flex justify-around">
                    <button className={"w-2/5 bg-white text-slate-800 rounded-sm font-semibold p-4 " + state[0]} onClick={() => reveal_answer(answer, set_state, question_number, question_total, question_setter)}>{options[0]}</button>
                    <button className={"w-2/5 bg-white text-slate-800 rounded-sm font-semibold p-4 " + state[1]} onClick={() => reveal_answer(answer, set_state, question_number, question_total, question_setter)}>{options[1]}</button>
                </div>
                <div className="flex justify-around mt-2">
                    <button className={"w-2/5 bg-white text-slate-800 rounded-sm font-semibold p-4 " + state[2]} onClick={() => reveal_answer(answer, set_state, question_number, question_total, question_setter)}>{options[2]}</button>
                    <button className={"w-2/5 bg-white text-slate-800 rounded-sm font-semibold p-4 " + state[3]} onClick={() => reveal_answer(answer, set_state, question_number, question_total, question_setter)}>{options[3]}</button>
                </div>
            </div>
        </div>
    )
}

function next_question(question_number: number, question_total: number): number {
    return question_number + 1 < question_total ? question_number + 1 : question_number
}

function reveal_answer(answer: number, set_state: React.Dispatch<React.SetStateAction<string[]>>, question_number: number, question_total: number, question_setter: React.Dispatch<React.SetStateAction<number>>) {
    let state = ["bg-red-700", "bg-red-700", "bg-red-700", "bg-red-700"];
    state[answer] = "bg-green-700";
    set_state(state)

    setTimeout(() => {
        let state = ["", "", "", ""];
        set_state(state);
        question_setter((question_number) => next_question(question_number, question_total))
    }, 3000);
}

export default Questionaire;
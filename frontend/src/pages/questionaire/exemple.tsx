import { useState } from "react";
import Questionaire from "../../components/questionaire";
import HomeButton from "../../components/homeButton";

function Exemple() {
    const [question_number, set_question_number] = useState(0);

    const questions = [
        "What is the capital of France?",
        "What is the capital of Germany?",
        "What is the capital of Italy?"
    ];

    const options: [string, string, string, string][] = [
        ["Paris", "London", "Berlin", "Rome"],
        ["Berlin", "Paris", "London", "Rome"],
        ["Rome", "London", "Berlin", "Paris"]
    ];

    const answers = [0, 0, 0];

    return (
        <div>
            <HomeButton />
            <div className="flex w-full justify-center h-full">
                <Questionaire question={questions[question_number]} options={options[question_number]} answer={answers[question_number]} question_number={question_number} question_total={3} question_setter={set_question_number} />
            </div>
        </div>
    )
}

export default Exemple;
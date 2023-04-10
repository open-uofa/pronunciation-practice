import React from 'react';

/**
 * Renders a chapter component that allows a student to click on a chapter to view its lessons.
 * 
 * @param {JSON} props.chapter - chapter object
 * @param {Function} props.onClick - function to call when the chapter is clicked
 * @returns {JSX.Element} - HomeChapter component consisting of a chapter name
 */
function HomeChapter(props) {
    return (
        <div className="chapter" onClick={props.onClick}>
            <p className="chapter-name">{props.chapter.name}</p>
        </div>
    );
}

export default HomeChapter;
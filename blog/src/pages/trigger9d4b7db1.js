import React, {useEffect} from "react";

const Trigger9d4b7db1 = () => {
    useEffect(() => {
        fetch("https://api.netlify.com/build_hooks/5cf88e880308f66f9d70c480", {method: "POST"})
    }, [])

    return <div>Build queued.</div>
}

console.log(Trigger9d4b7db1)

export default Trigger9d4b7db1

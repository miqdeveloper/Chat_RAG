io = io();

io.on("connect", () => {
   console.log(io.id); // x8WIv7-mJelg7on_ALbx
   io.emit("message", "Hello World from client");
 });
 
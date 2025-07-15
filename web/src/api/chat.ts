import service from "./request";

export function chat(content: string) {
  return service.post(`/chat/${content}`);
}
import { redirect } from 'next/navigation'

export default async function ProtectedPage() {


  return (
    <div className="flex h-svh w-full items-center justify-center gap-2">
      <p>
        Hello <span>{ }</span>
      </p>
    </div>
  )
}

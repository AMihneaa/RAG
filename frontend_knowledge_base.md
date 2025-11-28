# File: App.css

```css
#root {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.react:hover {
  filter: drop-shadow(0 0 2em #61dafbaa);
}

@media (prefers-color-scheme: light) {
  .dark {
    display: none; /* Hide light logo in light mode */
  }
}


@media (prefers-color-scheme: light) {
  .light {
    display: none; /* Hide dark logo in dark mode */
  }
}


@keyframes logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: no-preference) {
  a:nth-of-type(2) .logo {
    animation: logo-spin infinite 20s linear;
  }
}

.card {
  padding: 2em;
}

.read-the-docs {
  color: #888;
}

.input-box {
  width: 25%;
  border-radius: 5px;
  box-shadow: none !important;
  border: 2px solid #888;
  padding: 10px;
}
```


# File: App.tsx

```tsx
import "./App.css";

import { RouterProvider } from "react-router-dom";

import { router } from "./utils/Router";

export default function App() {

  return (
      <RouterProvider router={router}/>
  )
  
}

```


# File: component\footer.component.tsx

```tsx
import { Link } from "react-router-dom"
import { Bus} from "lucide-react"

export default function Footer() {
  return (
    <footer className="w-full border-t bg-background">
      <div className="container py-10">
        <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 md:grid-cols-4">
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <Bus className="h-5 w-5" />
              <span className="font-bold">Travel</span>
            </div>
            <p className="text-sm text-muted-foreground">Book your journey with ease and comfort.</p>
            <div className="flex space-x-3">
              <Link to="#" className="text-muted-foreground hover:text-foreground">
                <h1>Fb</h1>
                <span className="sr-only">Facebook</span>
              </Link>
              <Link to="#" className="text-muted-foreground hover:text-foreground">
                <h1>Twitter</h1>
                <span className="sr-only">Twitter</span>
              </Link>
              <Link to="#" className="text-muted-foreground hover:text-foreground">
                <h1>Instagram</h1>
                <span className="sr-only">Instagram</span>
              </Link>
            </div>
          </div>
          <div className="space-y-3">
            <h3 className="text-sm font-medium">Company</h3>
            <ul className="space-y-2">
              <li>
                <Link to="#" className="text-sm text-muted-foreground hover:text-foreground">
                  About Us
                </Link>
              </li>
              <li>
                <Link to="#" className="text-sm text-muted-foreground hover:text-foreground">
                  Careers
                </Link>
              </li>
              <li>
                <Link to="#" className="text-sm text-muted-foreground hover:text-foreground">
                  Press
                </Link>
              </li>
              <li>
                <Link to="#" className="text-sm text-muted-foreground hover:text-foreground">
                  News
                </Link>
              </li>
            </ul>
          </div>
          <div className="space-y-3">
            <h3 className="text-sm font-medium">Resources</h3>
            <ul className="space-y-2">
              <li>
                <Link to="#" className="text-sm text-muted-foreground hover:text-foreground">
                  Blog
                </Link>
              </li>
              <li>
                <Link to="#" className="text-sm text-muted-foreground hover:text-foreground">
                  Help Center
                </Link>
              </li>
              <li>
                <Link to="#" className="text-sm text-muted-foreground hover:text-foreground">
                  Safety Center
                </Link>
              </li>
              <li>
                <Link to="#" className="text-sm text-muted-foreground hover:text-foreground">
                  Community Guidelines
                </Link>
              </li>
            </ul>
          </div>
          <div className="space-y-3">
            <h3 className="text-sm font-medium">Legal</h3>
            <ul className="space-y-2">
              <li>
                <Link to="#" className="text-sm text-muted-foreground hover:text-foreground">
                  Terms of Service
                </Link>
              </li>
              <li>
                <Link to="#" className="text-sm text-muted-foreground hover:text-foreground">
                  Privacy Policy
                </Link>
              </li>
              <li>
                <Link to="#" className="text-sm text-muted-foreground hover:text-foreground">
                  Cookie Policy
                </Link>
              </li>
              <li>
                <Link to="#" className="text-sm text-muted-foreground hover:text-foreground">
                  Accessibility
                </Link>
              </li>
            </ul>
          </div>
        </div>
        <div className="mt-8 border-t pt-8 text-center">
          <p className="text-xs text-muted-foreground">
            © {new Date().getFullYear()} Travel. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  )
}

```


# File: component\mode-toggle.component.tsx

```tsx
import { Moon, Sun } from "lucide-react"
import { useTheme } from "@/component/theme-provider.component"
import { Button } from "@/components/ui/button"

export function ModeToggle() {
  const { setTheme, theme } = useTheme()

  const toggle = () => {
    setTheme(theme === "light" ? "dark" : "light")
  }

  return (
    <Button onClick={toggle} variant="outline" size="icon">
      <Sun className="h-4 w-4 rotate-0 scale-100 dark:-rotate-90 dark:scale-0" />
      <Moon className="absolute h-4 w-4 rotate-90 scale-0 dark:rotate-0 dark:scale-100" />
      <span className="sr-only">Toggle theme</span>
    </Button>
  )
}

```


# File: component\navbar.component.tsx

```tsx
import { useState } from "react"
import { Link, useLocation } from "react-router-dom"
import { Menu, X, Bus } from "lucide-react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { ModeToggle } from "@/component/mode-toggle.component"

export default function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const pathname = useLocation().pathname

  const routes = [
    { href: "/", label: "Home" },
    { href: "/routes/search", label: "Find Route" },
    { href: "/my-tickets", label: "My Tickets" },
  ]

  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center justify-between">
        <div className="flex items-center gap-2">
          <Link to="/" className="flex items-center gap-2">
            <Bus className="h-6 w-6" />
            <span className="hidden font-bold sm:inline-block">Travel</span>
          </Link>
        </div>

        <nav className="hidden md:flex items-center gap-6">
          {routes.map((route) => (
            <Link
              key={route.href}
              to={route.href}
              className={cn(
                "text-sm font-medium transition-colors hover:text-foreground/80",
                pathname === route.href ? "text-foreground" : "text-foreground/60"
              )}
            >
              {route.label}
            </Link>
          ))}
        </nav>

        <div className="flex items-center gap-2">
          <ModeToggle />
          <Button  className="hidden md:flex">
            <Link to="/login">Login</Link>
          </Button>
          <Button
            variant="outline"
            size="icon"
            className="md:hidden"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            {isMenuOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
          </Button>
        </div>
      </div>

      {isMenuOpen && (
        <div className="container md:hidden py-4">
          <nav className="flex flex-col gap-4">
            {routes.map((route) => (
              <Link
                key={route.href}
                to={route.href}
                className={cn(
                  "text-sm font-medium transition-colors hover:text-foreground/80",
                  pathname === route.href ? "text-foreground" : "text-foreground/60"
                )}
                onClick={() => setIsMenuOpen(false)}
              >
                {route.label}
              </Link>
            ))}
            <Button  className="w-full mt-2">
              <Link to="/login">Login</Link>
            </Button>
          </nav>
        </div>
      )}
    </header>
  )
}

```


# File: component\quick-search.component.tsx

```tsx
import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"

export default function QuickSearchSection() {
  const [departure, setDeparture] = useState("")
  const [arrival, setArrival] = useState("")
  const navigate = useNavigate()

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()

    if (!departure || !arrival) {
      alert("Please select both departure and arrival locations.")
      return
    }

    navigate("/routes/search", {
      state: { departure, arrival }
    })
  }

  return (
    <section className="container px-4 md:px-6">
      <div className="mx-auto max-w-3xl">
        <Card>
          <CardHeader>
            <CardTitle>Quick Search</CardTitle>
            <CardDescription>Find your route and book tickets instantly</CardDescription>
          </CardHeader>
          <CardContent>
            <form className="grid gap-4 sm:grid-cols-2 md:grid-cols-3" onSubmit={handleSubmit}>
              <div className="space-y-2">
                <label htmlFor="from" className="text-sm font-medium">From</label>
                <select
                  id="from"
                  className="form-select"
                  value={departure}
                  onChange={(e) => setDeparture(e.target.value)}
                >
                  <option value="">Select departure</option>
                  <option value="bucuresti">Bucuresti</option>
                  <option value="cluj">Cluj</option>
                  <option value="iasi">Iasi</option>
                  <option value="timisoara">Timisoara</option>
                </select>
              </div>
              <div className="space-y-2">
                <label htmlFor="to" className="text-sm font-medium">To</label>
                <select
                  id="to"
                  className="form-select"
                  value={arrival}
                  onChange={(e) => setArrival(e.target.value)}
                >
                  <option value="">Select destination</option>
                  <option value="constanta">Constanta</option>
                  <option value="brasov">Brasov</option>
                  <option value="sibiu">Sibiu</option>
                  <option value="pitesti">Pitesti</option>
                </select>
              </div>
              <div className="flex items-end">
                <Button type="submit" className="w-full">Search</Button>
              </div>
            </form>
          </CardContent>
        </Card>
      </div>
    </section>
  )
}

```


# File: component\route-result.component.tsx

```tsx
"use client"

import { useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion"
import { Clock, Bus, Train, Plane, Info, AlertCircle } from "lucide-react"
import { cn } from "@/lib/utils"
import { format, formatDistanceStrict, parseISO } from "date-fns"

interface Stop {
  location: string
  arrivalTime: string | null
  departureTime: string | null
}

interface Route {
  stops: Stop[]
  transportId: string
  transportType: "BUS" | "TRAIN" | "AIRPLANE"
  availableSeats: number
  id: string
  status: string
}

interface RouteResultsProps {
  routeOptions: Route[][]
}

export default function RouteResults({ routeOptions }: RouteResultsProps) {
  const [selectedTab, setSelectedTab] = useState("all")

  const filterByTransportType = (type: string) => {
    if (type === "all") return routeOptions
    return routeOptions.filter((routeList) => routeList.some((route) => route.transportType === type))
  }

  const filteredOptions = filterByTransportType(selectedTab)

  const getTransportIcon = (type: string) => {
    switch (type) {
      case "BUS":
        return <Bus className="h-4 w-4" />
      case "TRAIN":
        return <Train className="h-4 w-4" />
      case "AIRPLANE":
        return <Plane className="h-4 w-4" />
      default:
        return <Info className="h-4 w-4" />
    }
  }

  const getTransportColorClass = (type: string) => {
    switch (type) {
      case "BUS":
        return "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-300"
      case "TRAIN":
        return "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300"
      case "AIRPLANE":
        return "bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-300"
      default:
        return "bg-gray-100 text-gray-800 dark:bg-gray-800 dark:text-gray-300"
    }
  }

  const formatDateTime = (dateTimeString: string | null) => {
    if (!dateTimeString) return { time: "N/A", date: "N/A" }
    try {
      const date = parseISO(dateTimeString)
      return {
        time: format(date, "HH:mm"),
        date: format(date, "MMM d, yyyy"),
      }
    } catch (error) {
      return { time: "Invalid date", date: "Invalid date" }
    }
  }

  const calculateDuration = (startTime: string | null, endTime: string | null) => {
    if (!startTime || !endTime) return "Unknown"
    try {
      const start = parseISO(startTime)
      const end = parseISO(endTime)
      return formatDistanceStrict(end, start)
    } catch (error) {
      return "Invalid duration"
    }
  }

  const reserveTicket = async (transportIds: string[]) => {
    console.log("Reserving ticket for:", transportIds)
  
    const token = localStorage.getItem("Authorization")
  
    if (!token) {
      alert("You must be logged in to reserve tickets.")
      return
    }
  
    for (const routeID of transportIds) {
      try {
        const response = await fetch(
          `https://47287039-bf8e-4eb6-a406-71bfe9007b4f.eu-central-1.cloud.genez.io/reservation/user/route/${routeID}/ROUTE`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
          }
        )
  
        if (!response.ok) {
          const errorText = await response.text()
          console.error(`Failed to reserve for route ${routeID}:`, errorText)
          alert(`Error reserving route ${routeID}: ${errorText}`)
        } else {
          console.log(`Successfully reserved ticket for route ${routeID}`)
        }
      } catch (error) {
        console.error("Network error:", error)
        alert("Network error while reserving ticket.")
      }
    }
  
    alert("Reservation process completed!")
    window.location.replace("/my-tickets")
  }
  
  

  const getRouteEndpoints = (route: Route) => {
    if (!route.stops || route.stops.length === 0) {
      return { departure: "Unknown", arrival: "Unknown" }
    }
    return {
      departure: route.stops[0].location,
      arrival: route.stops[route.stops.length - 1].location,
    }
  }

  const getRouteTimes = (route: Route) => {
    if (!route.stops || route.stops.length === 0) {
      return { departureTime: null, arrivalTime: null }
    }

    const firstStop = route.stops[0]
    const lastStop = route.stops[route.stops.length - 1]

    return {
      departureTime: firstStop.departureTime,
      arrivalTime: lastStop.arrivalTime,
    }
  }

  const calculateOptionDetails = (routeOption: Route[]) => {
    if (routeOption.length === 0) {
      return {
        departureLocation: "Unknown",
        arrivalLocation: "Unknown",
        departureTime: null,
        arrivalTime: null,
        duration: "Unknown",
      }
    }

    const firstRoute = routeOption[0]
    const lastRoute = routeOption[routeOption.length - 1]

    const firstRouteEndpoints = getRouteEndpoints(firstRoute)
    const lastRouteEndpoints = getRouteEndpoints(lastRoute)

    const firstRouteTimes = getRouteTimes(firstRoute)
    const lastRouteTimes = getRouteTimes(lastRoute)

    return {
      departureLocation: firstRouteEndpoints.departure,
      arrivalLocation: lastRouteEndpoints.arrival,
      departureTime: firstRouteTimes.departureTime,
      arrivalTime: lastRouteTimes.arrivalTime,
      duration: calculateDuration(firstRouteTimes.departureTime, lastRouteTimes.arrivalTime),
    }
  }

  return (
    <div className="space-y-6">
      <Tabs defaultValue="all" value={selectedTab} onValueChange={setSelectedTab}>
        <TabsList>
          <TabsTrigger value="all">All</TabsTrigger>
          <TabsTrigger value="BUS" className="gap-2">
            <Bus className="h-4 w-4" /> Bus
          </TabsTrigger>
          <TabsTrigger value="TRAIN" className="gap-2">
            <Train className="h-4 w-4" /> Train
          </TabsTrigger>
          <TabsTrigger value="AIRPLANE" className="gap-2">
            <Plane className="h-4 w-4" /> Airplane
          </TabsTrigger>
        </TabsList>

        <TabsContent value={selectedTab} className="mt-6">
          {filteredOptions.length === 0 ? (
            <Card>
              <CardContent className="py-12 text-center">
                <p className="text-muted-foreground">No routes found for the selected transport type.</p>
              </CardContent>
            </Card>
          ) : (
            <div className="space-y-4">
              {filteredOptions.map((routeOption, optionIndex) => {
                const optionDetails = calculateOptionDetails(routeOption)
                const departureDateTime = formatDateTime(optionDetails.departureTime)
                const arrivalDateTime = formatDateTime(optionDetails.arrivalTime)

                return (
                  <Card key={optionIndex} className="overflow-hidden">
                    <CardHeader className="pb-0">
                      <div className="flex flex-wrap items-center justify-between gap-4">
                        <CardTitle className="text-lg">Option {optionIndex + 1}</CardTitle>
                        <div className="flex items-center gap-2">
                          <Badge variant="outline">
                            {routeOption.length > 1 ? `${routeOption.length} segments` : "Direct"}
                          </Badge>
                          {routeOption.map((route, i) => (
                            <Badge key={i} className={cn("text-xs", getTransportColorClass(route.transportType))}>
                              {route.transportType}
                            </Badge>
                          ))}
                        </div>
                      </div>
                    </CardHeader>
                    <CardContent className="pt-4">
                      <div className="grid gap-4 md:grid-cols-4">
                        <div className="space-y-1">
                          <div className="text-sm text-muted-foreground">From</div>
                          <div className="font-medium capitalize">{optionDetails.departureLocation}</div>
                          <div className="text-lg font-semibold">{departureDateTime.time}</div>
                          <div className="text-sm text-muted-foreground">{departureDateTime.date}</div>
                        </div>
                        <div className="space-y-1">
                          <div className="text-sm text-muted-foreground">To</div>
                          <div className="font-medium capitalize">{optionDetails.arrivalLocation}</div>
                          <div className="text-lg font-semibold">{arrivalDateTime.time}</div>
                          <div className="text-sm text-muted-foreground">{arrivalDateTime.date}</div>
                        </div>
                        <div className="space-y-1">
                          <div className="flex items-center gap-2">
                            <Clock className="h-4 w-4 text-muted-foreground" />
                            <span className="text-sm text-muted-foreground">Total Duration</span>
                          </div>
                          <div className="font-medium">{optionDetails.duration}</div>
                          <div className="text-sm text-muted-foreground">
                            {routeOption.length > 1
                              ? `${routeOption.length - 1} connection${routeOption.length > 2 ? "s" : ""}`
                              : "Direct route"}
                          </div>
                        </div>
                        <div className="flex flex-col items-end justify-between">
                          <div className="text-sm">
                            <Badge variant="outline">
                              {routeOption.reduce((total, route) => total + route.availableSeats, 0)} seats available
                            </Badge>
                          </div>
                          <Button
                            className="mt-2"
                            onClick={() => {
                                const transportIds = routeOption.map((route) => route.id)
                                reserveTicket(transportIds)
                            }}
                            >
                            Select
                            </Button>
                        </div>
                      </div>

                      {routeOption.length > 0 && (
                        <Accordion type="single" collapsible className="mt-4">
                          <AccordionItem value="segments">
                            <AccordionTrigger>View Route Details</AccordionTrigger>
                            <AccordionContent>
                              <div className="space-y-6 pt-2">
                                {routeOption.map((route, index) => {
                                  const routeEndpoints = getRouteEndpoints(route)
                                  const routeTimes = getRouteTimes(route)
                                  const departureInfo = formatDateTime(routeTimes.departureTime)
                                  const arrivalInfo = formatDateTime(routeTimes.arrivalTime)

                                  return (
                                    <div key={index} className="border-t pt-4 first:border-t-0 first:pt-0">
                                      <div className="flex items-center gap-2 mb-4">
                                        <div
                                          className={cn(
                                            "rounded-full p-1",
                                            getTransportColorClass(route.transportType),
                                          )}
                                        >
                                          {getTransportIcon(route.transportType)}
                                        </div>
                                        <span className="font-medium">{route.transportType}</span>
                                        <span className="text-xs text-muted-foreground">ID: {route.transportId}</span>
                                        <Badge
                                          variant="outline"
                                          className={
                                            route.status === "ACTIVE"
                                              ? "bg-green-100 text-green-800"
                                              : "bg-amber-100 text-amber-800"
                                          }
                                        >
                                          {route.status}
                                        </Badge>
                                        <Badge className="ml-auto">{route.availableSeats} seats</Badge>
                                      </div>

                                      <div className="space-y-4">
                                        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                                          <div className="space-y-1">
                                            <div className="text-sm text-muted-foreground">From</div>
                                            <div className="font-medium capitalize">{routeEndpoints.departure}</div>
                                            <div className="text-sm">{departureInfo.time}</div>
                                          </div>
                                          <div className="space-y-1">
                                            <div className="text-sm text-muted-foreground">To</div>
                                            <div className="font-medium capitalize">{routeEndpoints.arrival}</div>
                                            <div className="text-sm">{arrivalInfo.time}</div>
                                          </div>
                                          <div className="space-y-1">
                                            <div className="text-sm text-muted-foreground">Duration</div>
                                            <div className="font-medium">
                                              {calculateDuration(routeTimes.departureTime, routeTimes.arrivalTime)}
                                            </div>
                                          </div>
                                          <div className="space-y-1">
                                            <div className="text-sm text-muted-foreground">Stops</div>
                                            <div className="font-medium">
                                              {route.stops.length - 2} intermediate stops
                                            </div>
                                          </div>
                                        </div>

                                        {route.stops.length > 0 && (
                                          <div className="mt-4">
                                            <h4 className="text-sm font-medium mb-2">Stop Details</h4>
                                            <div className="space-y-2">
                                              {route.stops.map((stop, stopIndex) => {
                                                const stopArrival = formatDateTime(stop.arrivalTime)
                                                const stopDeparture = formatDateTime(stop.departureTime)

                                                return (
                                                  <div
                                                    key={stopIndex}
                                                    className="flex items-start gap-2 p-2 rounded-md bg-muted/50"
                                                  >
                                                    <div
                                                      className={cn(
                                                        "mt-1 h-2 w-2 rounded-full",
                                                        stopIndex === 0
                                                          ? "bg-green-500"
                                                          : stopIndex === route.stops.length - 1
                                                            ? "bg-red-500"
                                                            : "bg-blue-500",
                                                      )}
                                                    />
                                                    <div className="flex-1">
                                                      <div className="flex justify-between">
                                                        <span className="font-medium capitalize">{stop.location}</span>
                                                        <span className="text-xs text-muted-foreground">
                                                          {stopIndex === 0
                                                            ? "Departure"
                                                            : stopIndex === route.stops.length - 1
                                                              ? "Arrival"
                                                              : "Stop"}
                                                        </span>
                                                      </div>
                                                      <div className="flex justify-between text-sm">
                                                        <div>
                                                          {stop.arrivalTime && (
                                                            <span className="text-muted-foreground">
                                                              Arrival: {stopArrival.time}
                                                            </span>
                                                          )}
                                                        </div>
                                                        <div>
                                                          {stop.departureTime && (
                                                            <span className="text-muted-foreground">
                                                              Departure: {stopDeparture.time}
                                                            </span>
                                                          )}
                                                        </div>
                                                      </div>
                                                    </div>
                                                  </div>
                                                )
                                              })}
                                            </div>
                                          </div>
                                        )}
                                      </div>

                                      {index < routeOption.length - 1 && (
                                        <div className="flex items-center justify-center my-4">
                                          <div className="flex items-center gap-2 px-4 py-2 rounded-md bg-amber-100 text-amber-800">
                                            <AlertCircle className="h-4 w-4" />
                                            <span className="text-sm font-medium">Connection required</span>
                                          </div>
                                        </div>
                                      )}
                                    </div>
                                  )
                                })}
                              </div>
                            </AccordionContent>
                          </AccordionItem>
                        </Accordion>
                      )}
                    </CardContent>
                  </Card>
                )
              })}
            </div>
          )}
        </TabsContent>
      </Tabs>
    </div>
  )
}

```


# File: component\route-search-form.component.tsx

```tsx
import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

interface RouteSearchFormProps {
  onSearch: (departure: string, arrival: string) => void
  isLoading: boolean
}

export default function RouteSearchForm({ onSearch, isLoading }: RouteSearchFormProps) {
  const [departure, setDeparture] = useState("")
  const [arrival, setArrival] = useState("")

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (departure.trim() && arrival.trim()) {
      onSearch(departure.trim(), arrival.trim())
    }
  }

  return (
    <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-3 gap-4 items-end">
      <div>
        <label className="block text-sm font-medium text-muted-foreground mb-1">From</label>
        <Input
          type="text"
          placeholder="Departure location"
          value={departure}
          onChange={(e) => setDeparture(e.target.value)}
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-muted-foreground mb-1">To</label>
        <Input
          type="text"
          placeholder="Arrival location"
          value={arrival}
          onChange={(e) => setArrival(e.target.value)}
        />
      </div>
      <div>
        <Button type="submit" className="w-full" disabled={isLoading}>
          {isLoading ? "Searching..." : "Search"}
        </Button>
      </div>
    </form>
  )
}

```


# File: component\theme-provider.component.tsx

```tsx
import { createContext, useEffect, useState, useContext, ReactNode } from "react"

type Theme = "light" | "dark"

interface ThemeContextType {
  theme: Theme
  setTheme: (theme: Theme) => void
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined)

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [theme, setTheme] = useState<Theme>(() => {
    try {
      const stored = localStorage.getItem("theme")
      return stored === "light" || stored === "dark" ? stored : "light"
    } catch {
      return "light"
    }
  })

  useEffect(() => {
    try {
      if (theme === "light" || theme === "dark") {
        document.body.classList.remove("light", "dark")
        document.body.classList.add(theme)
        localStorage.setItem("theme", theme)
      }
    } catch (error) {
      console.error("💥 Error applying theme:", error)
    }
  }, [theme])  

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  )
}

export function useTheme() {
  const context = useContext(ThemeContext)
  if (!context) {
    throw new Error("useTheme must be used within a ThemeProvider")
  }
  return context
}

```


# File: components\ui\accordion.tsx

```tsx
import * as React from "react"
import * as AccordionPrimitive from "@radix-ui/react-accordion"
import { ChevronDownIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Accordion({
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Root>) {
  return <AccordionPrimitive.Root data-slot="accordion" {...props} />
}

function AccordionItem({
  className,
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Item>) {
  return (
    <AccordionPrimitive.Item
      data-slot="accordion-item"
      className={cn("border-b last:border-b-0", className)}
      {...props}
    />
  )
}

function AccordionTrigger({
  className,
  children,
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Trigger>) {
  return (
    <AccordionPrimitive.Header className="flex">
      <AccordionPrimitive.Trigger
        data-slot="accordion-trigger"
        className={cn(
          "focus-visible:border-ring focus-visible:ring-ring/50 flex flex-1 items-start justify-between gap-4 rounded-md py-4 text-left text-sm font-medium transition-all outline-none hover:underline focus-visible:ring-[3px] disabled:pointer-events-none disabled:opacity-50 [&[data-state=open]>svg]:rotate-180",
          className
        )}
        {...props}
      >
        {children}
        <ChevronDownIcon className="text-muted-foreground pointer-events-none size-4 shrink-0 translate-y-0.5 transition-transform duration-200" />
      </AccordionPrimitive.Trigger>
    </AccordionPrimitive.Header>
  )
}

function AccordionContent({
  className,
  children,
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Content>) {
  return (
    <AccordionPrimitive.Content
      data-slot="accordion-content"
      className="data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down overflow-hidden text-sm"
      {...props}
    >
      <div className={cn("pt-0 pb-4", className)}>{children}</div>
    </AccordionPrimitive.Content>
  )
}

export { Accordion, AccordionItem, AccordionTrigger, AccordionContent }

```


# File: components\ui\alert.tsx

```tsx
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const alertVariants = cva(
  "relative w-full rounded-lg border px-4 py-3 text-sm grid has-[>svg]:grid-cols-[calc(var(--spacing)*4)_1fr] grid-cols-[0_1fr] has-[>svg]:gap-x-3 gap-y-0.5 items-start [&>svg]:size-4 [&>svg]:translate-y-0.5 [&>svg]:text-current",
  {
    variants: {
      variant: {
        default: "bg-card text-card-foreground",
        destructive:
          "text-destructive bg-card [&>svg]:text-current *:data-[slot=alert-description]:text-destructive/90",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

function Alert({
  className,
  variant,
  ...props
}: React.ComponentProps<"div"> & VariantProps<typeof alertVariants>) {
  return (
    <div
      data-slot="alert"
      role="alert"
      className={cn(alertVariants({ variant }), className)}
      {...props}
    />
  )
}

function AlertTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="alert-title"
      className={cn(
        "col-start-2 line-clamp-1 min-h-4 font-medium tracking-tight",
        className
      )}
      {...props}
    />
  )
}

function AlertDescription({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="alert-description"
      className={cn(
        "text-muted-foreground col-start-2 grid justify-items-start gap-1 text-sm [&_p]:leading-relaxed",
        className
      )}
      {...props}
    />
  )
}

export { Alert, AlertTitle, AlertDescription }

```


# File: components\ui\badge.tsx

```tsx
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const badgeVariants = cva(
  "inline-flex items-center justify-center rounded-md border px-2 py-0.5 text-xs font-medium w-fit whitespace-nowrap shrink-0 [&>svg]:size-3 gap-1 [&>svg]:pointer-events-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive transition-[color,box-shadow] overflow-hidden",
  {
    variants: {
      variant: {
        default:
          "border-transparent bg-primary text-primary-foreground [a&]:hover:bg-primary/90",
        secondary:
          "border-transparent bg-secondary text-secondary-foreground [a&]:hover:bg-secondary/90",
        destructive:
          "border-transparent bg-destructive text-white [a&]:hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
        outline:
          "text-foreground [a&]:hover:bg-accent [a&]:hover:text-accent-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

function Badge({
  className,
  variant,
  asChild = false,
  ...props
}: React.ComponentProps<"span"> &
  VariantProps<typeof badgeVariants> & { asChild?: boolean }) {
  const Comp = asChild ? Slot : "span"

  return (
    <Comp
      data-slot="badge"
      className={cn(badgeVariants({ variant }), className)}
      {...props}
    />
  )
}

export { Badge, badgeVariants }

```


# File: components\ui\button.tsx

```tsx
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

export const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground shadow-xs hover:bg-primary/90",
        destructive: "bg-destructive text-white shadow-xs hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
        outline: "border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50",
        secondary: "bg-secondary text-secondary-foreground shadow-xs hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2 has-[>svg]:px-3",
        sm: "h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5",
        lg: "h-10 rounded-md px-6 has-[>svg]:px-4",
        icon: "size-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"

    return (
      <Comp
        className={cn(buttonVariants({ variant, size }), className)}
        ref={ref}
        {...props}
      />
    )
  }
)

Button.displayName = "Button"

export { Button }

```


# File: components\ui\card.tsx

```tsx
import * as React from "react"

import { cn } from "@/lib/utils"

function Card({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card"
      className={cn(
        "bg-card text-card-foreground flex flex-col gap-6 rounded-xl border py-6 shadow-sm",
        className
      )}
      {...props}
    />
  )
}

function CardHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-header"
      className={cn(
        "@container/card-header grid auto-rows-min grid-rows-[auto_auto] items-start gap-1.5 px-6 has-data-[slot=card-action]:grid-cols-[1fr_auto] [.border-b]:pb-6",
        className
      )}
      {...props}
    />
  )
}

function CardTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-title"
      className={cn("leading-none font-semibold", className)}
      {...props}
    />
  )
}

function CardDescription({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-description"
      className={cn("text-muted-foreground text-sm", className)}
      {...props}
    />
  )
}

function CardAction({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-action"
      className={cn(
        "col-start-2 row-span-2 row-start-1 self-start justify-self-end",
        className
      )}
      {...props}
    />
  )
}

function CardContent({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-content"
      className={cn("px-6", className)}
      {...props}
    />
  )
}

function CardFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-footer"
      className={cn("flex items-center px-6 [.border-t]:pt-6", className)}
      {...props}
    />
  )
}

export {
  Card,
  CardHeader,
  CardFooter,
  CardTitle,
  CardAction,
  CardDescription,
  CardContent,
}

```


# File: components\ui\dropdown-menu.tsx

```tsx
import * as React from "react"
import * as DropdownMenuPrimitive from "@radix-ui/react-dropdown-menu"
import { CheckIcon, ChevronRightIcon, CircleIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function DropdownMenu({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Root>) {
  return <DropdownMenuPrimitive.Root data-slot="dropdown-menu" {...props} />
}

function DropdownMenuPortal({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Portal>) {
  return (
    <DropdownMenuPrimitive.Portal data-slot="dropdown-menu-portal" {...props} />
  )
}

function DropdownMenuTrigger({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Trigger>) {
  return (
    <DropdownMenuPrimitive.Trigger
      data-slot="dropdown-menu-trigger"
      {...props}
    />
  )
}

function DropdownMenuContent({
  className,
  sideOffset = 4,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Content>) {
  return (
    <DropdownMenuPrimitive.Portal>
      <DropdownMenuPrimitive.Content
        data-slot="dropdown-menu-content"
        sideOffset={sideOffset}
        className={cn(
          "bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 max-h-(--radix-dropdown-menu-content-available-height) min-w-[8rem] origin-(--radix-dropdown-menu-content-transform-origin) overflow-x-hidden overflow-y-auto rounded-md border p-1 shadow-md",
          className
        )}
        {...props}
      />
    </DropdownMenuPrimitive.Portal>
  )
}

function DropdownMenuGroup({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Group>) {
  return (
    <DropdownMenuPrimitive.Group data-slot="dropdown-menu-group" {...props} />
  )
}

function DropdownMenuItem({
  className,
  inset,
  variant = "default",
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Item> & {
  inset?: boolean
  variant?: "default" | "destructive"
}) {
  return (
    <DropdownMenuPrimitive.Item
      data-slot="dropdown-menu-item"
      data-inset={inset}
      data-variant={variant}
      className={cn(
        "focus:bg-accent focus:text-accent-foreground data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 dark:data-[variant=destructive]:focus:bg-destructive/20 data-[variant=destructive]:focus:text-destructive data-[variant=destructive]:*:[svg]:!text-destructive [&_svg:not([class*='text-'])]:text-muted-foreground relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 data-[inset]:pl-8 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    />
  )
}

function DropdownMenuCheckboxItem({
  className,
  children,
  checked,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.CheckboxItem>) {
  return (
    <DropdownMenuPrimitive.CheckboxItem
      data-slot="dropdown-menu-checkbox-item"
      className={cn(
        "focus:bg-accent focus:text-accent-foreground relative flex cursor-default items-center gap-2 rounded-sm py-1.5 pr-2 pl-8 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      checked={checked}
      {...props}
    >
      <span className="pointer-events-none absolute left-2 flex size-3.5 items-center justify-center">
        <DropdownMenuPrimitive.ItemIndicator>
          <CheckIcon className="size-4" />
        </DropdownMenuPrimitive.ItemIndicator>
      </span>
      {children}
    </DropdownMenuPrimitive.CheckboxItem>
  )
}

function DropdownMenuRadioGroup({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.RadioGroup>) {
  return (
    <DropdownMenuPrimitive.RadioGroup
      data-slot="dropdown-menu-radio-group"
      {...props}
    />
  )
}

function DropdownMenuRadioItem({
  className,
  children,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.RadioItem>) {
  return (
    <DropdownMenuPrimitive.RadioItem
      data-slot="dropdown-menu-radio-item"
      className={cn(
        "focus:bg-accent focus:text-accent-foreground relative flex cursor-default items-center gap-2 rounded-sm py-1.5 pr-2 pl-8 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    >
      <span className="pointer-events-none absolute left-2 flex size-3.5 items-center justify-center">
        <DropdownMenuPrimitive.ItemIndicator>
          <CircleIcon className="size-2 fill-current" />
        </DropdownMenuPrimitive.ItemIndicator>
      </span>
      {children}
    </DropdownMenuPrimitive.RadioItem>
  )
}

function DropdownMenuLabel({
  className,
  inset,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Label> & {
  inset?: boolean
}) {
  return (
    <DropdownMenuPrimitive.Label
      data-slot="dropdown-menu-label"
      data-inset={inset}
      className={cn(
        "px-2 py-1.5 text-sm font-medium data-[inset]:pl-8",
        className
      )}
      {...props}
    />
  )
}

function DropdownMenuSeparator({
  className,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Separator>) {
  return (
    <DropdownMenuPrimitive.Separator
      data-slot="dropdown-menu-separator"
      className={cn("bg-border -mx-1 my-1 h-px", className)}
      {...props}
    />
  )
}

function DropdownMenuShortcut({
  className,
  ...props
}: React.ComponentProps<"span">) {
  return (
    <span
      data-slot="dropdown-menu-shortcut"
      className={cn(
        "text-muted-foreground ml-auto text-xs tracking-widest",
        className
      )}
      {...props}
    />
  )
}

function DropdownMenuSub({
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.Sub>) {
  return <DropdownMenuPrimitive.Sub data-slot="dropdown-menu-sub" {...props} />
}

function DropdownMenuSubTrigger({
  className,
  inset,
  children,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.SubTrigger> & {
  inset?: boolean
}) {
  return (
    <DropdownMenuPrimitive.SubTrigger
      data-slot="dropdown-menu-sub-trigger"
      data-inset={inset}
      className={cn(
        "focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground flex cursor-default items-center rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-[inset]:pl-8",
        className
      )}
      {...props}
    >
      {children}
      <ChevronRightIcon className="ml-auto size-4" />
    </DropdownMenuPrimitive.SubTrigger>
  )
}

function DropdownMenuSubContent({
  className,
  ...props
}: React.ComponentProps<typeof DropdownMenuPrimitive.SubContent>) {
  return (
    <DropdownMenuPrimitive.SubContent
      data-slot="dropdown-menu-sub-content"
      className={cn(
        "bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 min-w-[8rem] origin-(--radix-dropdown-menu-content-transform-origin) overflow-hidden rounded-md border p-1 shadow-lg",
        className
      )}
      {...props}
    />
  )
}

export {
  DropdownMenu,
  DropdownMenuPortal,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuLabel,
  DropdownMenuItem,
  DropdownMenuCheckboxItem,
  DropdownMenuRadioGroup,
  DropdownMenuRadioItem,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuSub,
  DropdownMenuSubTrigger,
  DropdownMenuSubContent,
}

```


# File: components\ui\input.tsx

```tsx
import * as React from "react"

import { cn } from "@/lib/utils"

function Input({ className, type, ...props }: React.ComponentProps<"input">) {
  return (
    <input
      type={type}
      data-slot="input"
      className={cn(
        "file:text-foreground placeholder:text-muted-foreground selection:bg-primary selection:text-primary-foreground dark:bg-input/30 border-input flex h-9 w-full min-w-0 rounded-md border bg-transparent px-3 py-1 text-base shadow-xs transition-[color,box-shadow] outline-none file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
        "focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px]",
        "aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
        className
      )}
      {...props}
    />
  )
}

export { Input }

```


# File: components\ui\sonner.tsx

```tsx
import { useTheme } from "next-themes"
import { Toaster as Sonner, ToasterProps } from "sonner"

const Toaster = ({ ...props }: ToasterProps) => {
  const { theme = "system" } = useTheme()

  return (
    <Sonner
      theme={theme as ToasterProps["theme"]}
      className="toaster group"
      style={
        {
          "--normal-bg": "var(--popover)",
          "--normal-text": "var(--popover-foreground)",
          "--normal-border": "var(--border)",
        } as React.CSSProperties
      }
      {...props}
    />
  )
}

export { Toaster }

```


# File: components\ui\tabs.tsx

```tsx
import * as React from "react"
import * as TabsPrimitive from "@radix-ui/react-tabs"

import { cn } from "@/lib/utils"

function Tabs({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.Root>) {
  return (
    <TabsPrimitive.Root
      data-slot="tabs"
      className={cn("flex flex-col gap-2", className)}
      {...props}
    />
  )
}

function TabsList({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.List>) {
  return (
    <TabsPrimitive.List
      data-slot="tabs-list"
      className={cn(
        "bg-muted text-muted-foreground inline-flex h-9 w-fit items-center justify-center rounded-lg p-[3px]",
        className
      )}
      {...props}
    />
  )
}

function TabsTrigger({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.Trigger>) {
  return (
    <TabsPrimitive.Trigger
      data-slot="tabs-trigger"
      className={cn(
        "data-[state=active]:bg-background dark:data-[state=active]:text-foreground focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:outline-ring dark:data-[state=active]:border-input dark:data-[state=active]:bg-input/30 text-foreground dark:text-muted-foreground inline-flex h-[calc(100%-1px)] flex-1 items-center justify-center gap-1.5 rounded-md border border-transparent px-2 py-1 text-sm font-medium whitespace-nowrap transition-[color,box-shadow] focus-visible:ring-[3px] focus-visible:outline-1 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:shadow-sm [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    />
  )
}

function TabsContent({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.Content>) {
  return (
    <TabsPrimitive.Content
      data-slot="tabs-content"
      className={cn("flex-1 outline-none", className)}
      {...props}
    />
  )
}

export { Tabs, TabsList, TabsTrigger, TabsContent }

```


# File: components\ui\toggle.tsx

```tsx
import * as React from "react"
import * as TogglePrimitive from "@radix-ui/react-toggle"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const toggleVariants = cva(
  "inline-flex items-center justify-center gap-2 rounded-md text-sm font-medium hover:bg-muted hover:text-muted-foreground disabled:pointer-events-none disabled:opacity-50 data-[state=on]:bg-accent data-[state=on]:text-accent-foreground [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 [&_svg]:shrink-0 focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] outline-none transition-[color,box-shadow] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive whitespace-nowrap",
  {
    variants: {
      variant: {
        default: "bg-transparent",
        outline:
          "border border-input bg-transparent shadow-xs hover:bg-accent hover:text-accent-foreground",
      },
      size: {
        default: "h-9 px-2 min-w-9",
        sm: "h-8 px-1.5 min-w-8",
        lg: "h-10 px-2.5 min-w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Toggle({
  className,
  variant,
  size,
  ...props
}: React.ComponentProps<typeof TogglePrimitive.Root> &
  VariantProps<typeof toggleVariants>) {
  return (
    <TogglePrimitive.Root
      data-slot="toggle"
      className={cn(toggleVariants({ variant, size, className }))}
      {...props}
    />
  )
}

export { Toggle, toggleVariants }

```


# File: hooks\use-auth.tsx

```tsx
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export function useAuth() {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem("Authorization");
    setIsAuthenticated(!!token);
  }, []);

  const login = (token: string) => {
    localStorage.setItem("Authorization", token);
    setIsAuthenticated(true);
  };

  const logout = () => {
    localStorage.removeItem("Authorization");
    setIsAuthenticated(false);
    router.push("/login");
  };

  return {
    isAuthenticated,
    login,
    logout,
  };
}
```


# File: index.css

```css
@import "tailwindcss";
@import "tw-animate-css";
/* 
---break--- */
@custom-variant dark (&:is(.dark *));


@layer base {
  body {
    @apply bg-background text-foreground;
  }
}


/* 
root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

a {
  font-weight: 500;
  color: #646cff;
  text-decoration: inherit;
}
a:hover {
  color: #535bf2;
}

body {
  margin: 0;
  display: flex;
  place-items: center;
  min-width: 320px;
  min-height: 100vh;
}

h1 {
  font-size: 3.2em;
  line-height: 1.1;
}

button {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  background-color: #1a1a1a;
  cursor: pointer;
  transition: border-color 0.25s;
}
button:hover {
  border-color: #646cff;
}
button:focus,
button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}

@media (prefers-color-scheme: light) {
  :root {
    color: #213547;
    background-color: #ffffff;
  }
  a:hover {
    color: #747bff;
  }
  button {
    background-color: #f9f9f9;
  }
} 
/* 
---break--- */
@theme inline {
  --radius-sm: calc(var(--radius) - 4px);
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 4px);
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-chart-1: var(--chart-1);
  --color-chart-2: var(--chart-2);
  --color-chart-3: var(--chart-3);
  --color-chart-4: var(--chart-4);
  --color-chart-5: var(--chart-5);
  --color-sidebar: var(--sidebar);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-sidebar-primary: var(--sidebar-primary);
  --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
  --color-sidebar-accent: var(--sidebar-accent);
  --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
  --color-sidebar-border: var(--sidebar-border);
  --color-sidebar-ring: var(--sidebar-ring);
}
/* 
---break--- */
:root {
  --radius: 0.625rem;
  --background: oklch(1 0 0);
  --foreground: oklch(0.145 0 0);
  --card: oklch(1 0 0);
  --card-foreground: oklch(0.145 0 0);
  --popover: oklch(1 0 0);
  --popover-foreground: oklch(0.145 0 0);
  --primary: oklch(0.205 0 0);
  --primary-foreground: oklch(0.985 0 0);
  --secondary: oklch(0.97 0 0);
  --secondary-foreground: oklch(0.205 0 0);
  --muted: oklch(0.97 0 0);
  --muted-foreground: oklch(0.556 0 0);
  --accent: oklch(0.97 0 0);
  --accent-foreground: oklch(0.205 0 0);
  --destructive: oklch(0.577 0.245 27.325);
  --border: oklch(0.922 0 0);
  --input: oklch(0.922 0 0);
  --ring: oklch(0.708 0 0);
  --chart-1: oklch(0.646 0.222 41.116);
  --chart-2: oklch(0.6 0.118 184.704);
  --chart-3: oklch(0.398 0.07 227.392);
  --chart-4: oklch(0.828 0.189 84.429);
  --chart-5: oklch(0.769 0.188 70.08);
  --sidebar: oklch(0.985 0 0);
  --sidebar-foreground: oklch(0.145 0 0);
  --sidebar-primary: oklch(0.205 0 0);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.97 0 0);
  --sidebar-accent-foreground: oklch(0.205 0 0);
  --sidebar-border: oklch(0.922 0 0);
  --sidebar-ring: oklch(0.708 0 0);
}
/* 
---break--- */
.dark {
  --background: oklch(0.18 0.01 260); /* dark navy-gray */
  --foreground: oklch(0.95 0.005 260); /* almost white text */

  --card: oklch(0.21 0.01 260);
  --card-foreground: var(--foreground);

  --popover: oklch(0.22 0.015 260);
  --popover-foreground: var(--foreground);

  --primary: oklch(0.7 0.15 250); /* soft blue */
  --primary-foreground: oklch(0.98 0.01 260); /* off-white */

  --secondary: oklch(0.3 0.02 260); /* subtle dark grey-blue */
  --secondary-foreground: var(--foreground);

  --muted: oklch(0.28 0.01 260);
  --muted-foreground: oklch(0.65 0.015 260);

  --accent: oklch(0.32 0.03 260);
  --accent-foreground: var(--foreground);

  --destructive: oklch(0.5 0.2 25); /* softer red */
  --destructive-foreground: oklch(0.98 0.01 260);

  --border: oklch(0.25 0.01 260 / 0.2);
  --input: oklch(0.25 0.01 260 / 0.2);
  --ring: oklch(0.7 0.15 250); /* match primary */

  --chart-1: oklch(0.6 0.2 260);
  --chart-2: oklch(0.6 0.15 200);
  --chart-3: oklch(0.7 0.13 100);
  --chart-4: oklch(0.7 0.14 340);
  --chart-5: oklch(0.6 0.17 60);

  --sidebar: oklch(0.19 0.01 260);
  --sidebar-foreground: var(--foreground);
  --sidebar-primary: var(--primary);
  --sidebar-primary-foreground: var(--primary-foreground);
  --sidebar-accent: oklch(0.27 0.03 280);
  --sidebar-accent-foreground: var(--foreground);
  --sidebar-border: var(--border);
  --sidebar-ring: var(--ring);
}

/* 
---break--- */
@layer base {
  * {
    @apply border-border outline-ring/50;
  }
  body {
    @apply bg-background text-foreground;
  }
}

```


# File: lib\types.ts

```ts
export interface Route {
    id: number | string
    from: string
    to: string
    price: string | number
    duration: string
    departures: string
    departureTime?: string
    arrivalTime?: string
    rating?: number
    amenities?: string[]
    popular?: boolean
  }
  
  export interface Ticket {
    id: string
    from: string
    to: string
    date: string
    departureTime: string
    arrivalTime: string
    passengers: number
    status: "upcoming" | "completed" | "cancelled"
    price: string
  }

  export interface ReservationDetails {
    [reservationId: string]: {
      [transportType: string]: {
        "Reservation Status": "ACTIVE" | "INACTIVE";
        Routes: string[];
      };
    };
  }

  export interface NormalizedReservation {
    id: string;
    transportType: string;
    reservationStatus: "ACTIVE" | "INACTIVE";
    routes: string[];
  }
  
  export interface DepartureOption {
    time: string
    arrivalTime: string
    price: number
  }
```


# File: lib\utils.ts

```ts
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

```


# File: main.tsx

```tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

```


# File: pages\Home.pages.tsx

```tsx
import { Link } from "react-router-dom"
import { Button } from "@/components/ui/button"
import IMAGE from "@/assets/imagine1.jpg"
import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import {
  ArrowRight,
  Calendar,
  Clock,
} from "lucide-react"

import QuickSearchSection from "@/component/quick-search.component"

export default function HomePage() {
  const newsItems = [
    {
      id: 1,
      title: "New Express Routes Added",
      description: "We've added 5 new express routes connecting major cities with faster travel times.",
      date: "May 15",
      category: "Routes",
    },
    {
      id: 2,
      title: "Summer Discount Program",
      description: "Get up to 25% off on all tickets booked for summer travel between June and August.",
      date: "May 10",
      category: "Promotions",
    },
    {
      id: 3,
      title: "Mobile App Update",
      description: "Our mobile app now features real-time tracking and instant notifications for your journey.",
      date: "May 5",
      category: "Technology",
    },
  ]

  const popularRoutes = [
    { id: 1, from: "Bucuresti", to: "Constanta", price: "$25", duration: "1h 30m", departures: "Hourly" },
    { id: 2, from: "Pitesti", to: "Bucuresti", price: "$55", duration: "2h 15m", departures: "Every 2 hours" },
    { id: 3, from: "Pitesti", to: "Constanta", price: "$35", duration: "3h 45m", departures: "4 times daily" },
    { id: 4, from: "Cernavoda", to: "Bucuresti", price: "$30", duration: "1h 30m", departures: "6 times daily" },
  ]

  return (
    <div className="flex flex-col gap-12 pb-8">
      {/* Hero Section */}
      
      <section className="w-full py-12 md:py-24 lg:py-32 bg-muted">
        <div className="container px-4 md:px-6">
          <div className="grid gap-6 lg:grid-cols-2 lg:gap-12 items-center">
            <div className="space-y-4">
              <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
                Travel with Comfort and Convenience
              </h1>
              <p className="text-muted-foreground md:text-xl">
                Book tickets for your journey with ease. Choose from thousands of routes, compare prices, and secure
                your seat in minutes.
              </p>
              <div className="flex flex-col sm:flex-row gap-3">
                <Button size="lg">
                  <Link to="/routes">Find Routes</Link>
                </Button>
                <Button variant="outline" size="lg" >
                  <Link to="/my-tickets">My Tickets</Link>
                </Button>
              </div>
            </div>
            <div className="relative h-[300px] sm:h-[400px] lg:h-[500px] rounded-xl overflow-hidden">
              <img
                src= {IMAGE}
                alt="Comfortable bus travel"
                className="w-full h-full object-cover"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Search Section */}
      {/* <section className="container px-4 md:px-6">
        <div className="mx-auto max-w-3xl">
          <Card>
            <CardHeader>
              <CardTitle>Quick Search</CardTitle>
              <CardDescription>Find your route and book tickets instantly</CardDescription>
            </CardHeader>
            <CardContent>
              <form className="grid gap-4 sm:grid-cols-2 md:grid-cols-4">
                <div className="space-y-2">
                  <label htmlFor="from" className="text-sm font-medium">From</label>
                  <select id="from" className="form-select">
                    <option value="">Select departure</option>
                    <option value="new-york">New York</option>
                    <option value="los-angeles">Los Angeles</option>
                    <option value="chicago">Chicago</option>
                    <option value="miami">Miami</option>
                  </select>
                </div>
                <div className="space-y-2">
                  <label htmlFor="to" className="text-sm font-medium">To</label>
                  <select id="to" className="form-select">
                    <option value="">Select destination</option>
                    <option value="boston">Boston</option>
                    <option value="san-francisco">San Francisco</option>
                    <option value="detroit">Detroit</option>
                    <option value="orlando">Orlando</option>
                  </select>
                </div>
                <div className="space-y-2">
                  <label htmlFor="date" className="text-sm font-medium">Date</label>
                  <input type="date" id="date" className="form-input" />
                </div>
                <div className="flex items-end">
                  <Button className="w-full">Search</Button>
                </div>
              </form>
            </CardContent>
          </Card>
        </div>
      </section> */}
      <QuickSearchSection />

      {/* Popular Routes Section */}
      <section className="container px-4 md:px-6">
        <div className="flex flex-col gap-4">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-2xl font-bold tracking-tight">Popular Routes</h2>
              <p className="text-muted-foreground">Most frequently booked destinations</p>
            </div>
            <Button variant="ghost"  className="gap-1">
              <Link to="/routes">
                View all routes
                <ArrowRight className="h-4 w-4" />
              </Link>
            </Button>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {popularRoutes.map((route) => (
              <Card key={route.id}>
                <CardHeader className="p-4">
                  <CardTitle className="text-lg flex justify-between items-start">
                    <div>
                      <span>{route.from}</span>
                      <span className="text-muted-foreground text-sm"> to </span>
                      <span>{route.to}</span>
                    </div>
                    <Badge>{route.price}</Badge>
                  </CardTitle>
                </CardHeader>
                <CardContent className="p-4 pt-0 space-y-2">
                  <div className="flex items-center gap-2 text-sm">
                    <Clock className="h-4 w-4 text-muted-foreground" />
                    <span>{route.duration}</span>
                  </div>
                  <div className="flex items-center gap-2 text-sm">
                    <Calendar className="h-4 w-4 text-muted-foreground" />
                    <span>{route.departures}</span>
                  </div>
                </CardContent>
                <CardFooter className="p-4 pt-0">
                  <Button  className="w-full">
                    <Link to={`/routes/${route.id}`}>View Details</Link>
                  </Button>
                </CardFooter>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* News Section */}
      <section className="container px-4 md:px-6">
        <div className="flex flex-col gap-4">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-2xl font-bold tracking-tight">Latest News</h2>
              <p className="text-muted-foreground">Stay updated with Travel</p>
            </div>
            <Button variant="ghost"  className="gap-1">
              <Link to="/news">
                All news
                <ArrowRight className="h-4 w-4" />
              </Link>
            </Button>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {newsItems.map((item) => (
              <Card key={item.id}>
                <CardHeader className="pb-3">
                  <div className="flex items-center gap-2 mb-2">
                    <Badge variant="outline">{item.category}</Badge>
                    <span className="text-xs text-muted-foreground">{item.date}</span>
                  </div>
                  <CardTitle className="text-xl">{item.title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">{item.description}</p>
                </CardContent>
                <CardFooter>
                  <Button variant="ghost" size="sm" className="gap-1">
                    Read more
                    <ArrowRight className="h-4 w-4" />
                  </Button>
                </CardFooter>
              </Card>
            ))}
          </div>
        </div>
      </section>
    </div>
  )
}

```


# File: pages\layout.tsx

```tsx
import { Outlet } from "react-router-dom"
import Navbar from "@/component/navbar.component"
import Footer from "@/component/footer.component"
import { ThemeProvider } from "@/component/theme-provider.component"
import { Toaster } from "@/components/ui/sonner"

export default function RootLayout() {
  return (
    <ThemeProvider >
      <div className="bg-background font-sans antialiased min-h-screen">
        <Navbar />
        <main className="flex-1">
          <Outlet />
        </main>
        <Footer />
        <Toaster />
      </div>
    </ThemeProvider>
  )
}

```


# File: pages\not-found.page.tsx

```tsx
import { Link } from "react-router-dom"
import { Button } from "@/components/ui/button"
import { AlertTriangle } from "lucide-react"

export default function NotFound() {
  return (
    <div className="container flex flex-col items-center justify-center min-h-[70vh] px-4 py-16 text-center">
      <div className="mb-4 rounded-full bg-muted p-6">
        <AlertTriangle className="h-10 w-10 text-muted-foreground" />
      </div>
      <h1 className="text-4xl font-bold tracking-tight mb-2">Page Not Found</h1>
      <p className="text-muted-foreground mb-8 max-w-md">
        Sorry, we couldn't find the page you're looking for. It might have been moved, deleted, or never existed.
      </p>
      <div className="flex flex-col sm:flex-row gap-4">
        <Button  size="lg">
          <Link to="/">Go Home</Link>
        </Button>
        <Button variant="outline"  size="lg">
          <Link to="/routes">Browse Routes</Link>
        </Button>
      </div>
    </div>
  )
}

```


# File: pages\Search.pages.tsx

```tsx
import { useState } from "react"
import { useNavigate } from "react-router-dom"
import RouteSearchForm from "@/component/route-search-form.component"
import RouteResults from "@/component/route-result.component"
import { Card, CardContent } from "@/components/ui/card"
import { Loader2, AlertCircle } from "lucide-react"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { useLocation } from "react-router-dom"
import { useEffect } from "react"

interface Stop {
  location: string
  arrivalTime: string | null
  departureTime: string | null
}

interface Route {
  stops: Stop[]
  transportId: string
  transportType: "BUS" | "TRAIN" | "AIRPLANE"
  availableSeats: number
  id: string
  status: string
}

export default function RouteSearchPage() {
  const [routes, setRoutes] = useState<Route[][]>([])
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [searchPerformed, setSearchPerformed] = useState(false)

  const navigate = useNavigate()
  const location = useLocation()
  const { departure, arrival } = location.state || {}
  
  useEffect(() => {
    if (departure && arrival) {
      handleSearch(departure, arrival)
    }
  }, [departure, arrival])

  const isAuthenticated = !!localStorage.getItem("Authorization")

  const handleSearch = async (departure: string, arrival: string) => {
    if (!isAuthenticated) {
      navigate("/login?redirect=/routes/search")
      return
    }

    setIsLoading(true)
    setError(null)
    setSearchPerformed(true)

    try {
      const API_URL = import.meta.env.VITE_BACK_END_URL;
      const response = await fetch(
        `${API_URL}/reservation/user/${encodeURIComponent(departure)}/to/${encodeURIComponent(arrival)}`,
        {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("Authorization")}`,
          },
        }
      )

      if (!response.ok) {
        if (response.status === 401 || response.status === 403) {
          throw new Error("You are not authorized to view these routes. Please log in again.")
        } else if (response.status === 404) {
          throw new Error("No routes found for the selected locations.")
        } else {
          throw new Error("An error occurred while fetching routes.")
        }
      }

      const data = await response.json()
      setRoutes(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to fetch routes")
      setRoutes([])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="container px-4 md:px-6 py-8">
      <div className="flex flex-col gap-6">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Find Routes</h1>
          <p className="text-muted-foreground">Search for routes between locations</p>
        </div>

        <RouteSearchForm onSearch={handleSearch} isLoading={isLoading} />

        {isLoading && (
          <div className="flex justify-center py-12">
            <Loader2 className="h-8 w-8 animate-spin text-primary" />
            <span className="sr-only">Loading routes...</span>
          </div>
        )}

        {error && (
          <Alert variant="destructive">
            <AlertCircle className="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}

        {!isLoading && !error && searchPerformed && routes.length === 0 && (
          <Card>
            <CardContent className="py-12 text-center">
              <p className="text-muted-foreground">No routes found for the selected locations.</p>
              <p className="text-muted-foreground mt-1">Try different locations or check back later.</p>
            </CardContent>
          </Card>
        )}

        {!isLoading && !error && routes.length > 0 && (
          <div className="space-y-6">
            <div className="flex items-center justify-between">
              <h2 className="text-2xl font-bold">Available Routes</h2>
              <p className="text-muted-foreground">Found {routes.length} route options</p>
            </div>
            <RouteResults routeOptions={routes} />
          </div>
        )}
      </div>
    </div>
  )
}

```


# File: pages\Ticket.tsx

```tsx
import { useEffect, useState } from "react";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Calendar } from "lucide-react";
import { NormalizedReservation } from "@/lib/types";

export default function MyTicketsPage() {
  const [tickets, setTickets] = useState<NormalizedReservation[]>([]);

  useEffect(() => {
    const fetchTickets = async () => {
      try {
        const API_URL = import.meta.env.VITE_BACK_END_URL;
        const response = await fetch(`${API_URL}/reservation/user/myTicket`, {
          method: "GET",
          headers: {
            Authorization: `Bearer ${localStorage.getItem("Authorization")}`,
            "Content-Type": "application/json",
          },
        });

        const raw = await response.json() as Record<
          string,
          Record<
            string,
            {
              "Reservation Status": "ACTIVE" | "INACTIVE";
              "Routes": string[];
            }
          >
        >;

        const parsed: NormalizedReservation[] = Object.entries(raw).map(([id, transportMap]) => {
          const [transportType, details] = Object.entries(transportMap)[0];
          return {
            id,
            transportType,
            reservationStatus: details["Reservation Status"],
            routes: details["Routes"],
          };
        });

        setTickets(parsed);
      } catch (error) {
        console.error("Failed to fetch tickets:", error);
      }
    };

    fetchTickets();
  }, []);

  const upcoming = tickets.filter((t) => t.reservationStatus === "ACTIVE");
  const completed = tickets.filter((t) => t.reservationStatus === "INACTIVE");

  return (
    <div className="container px-4 py-8">
      <h1 className="text-3xl font-bold mb-4">My Tickets</h1>
      <Tabs defaultValue="upcoming" className="w-full">
        <TabsList className="mb-4 grid grid-cols-2 w-full">
          <TabsTrigger value="upcoming">Upcoming ({upcoming.length})</TabsTrigger>
          <TabsTrigger value="completed">Completed ({completed.length})</TabsTrigger>
        </TabsList>

        <TabsContent value="upcoming">
          <div className="space-y-4">
            {upcoming.map((ticket) => (
              <TicketCard key={ticket.id} ticket={ticket} />
            ))}
          </div>
        </TabsContent>

        <TabsContent value="completed">
          <div className="space-y-4">
            {completed.map((ticket) => (
              <TicketCard key={ticket.id} ticket={ticket} />
            ))}
          </div>
        </TabsContent>
      </Tabs>
    </div>
  );
}

function TicketCard({ ticket }: { ticket: NormalizedReservation }) {
  const from = ticket.routes[0];
  const to = ticket.routes[ticket.routes.length - 1];

  return (
    <Card>
      <CardContent className="p-4 flex flex-col gap-2">
        <div className="flex justify-between items-center">
          <Badge>{ticket.reservationStatus}</Badge>
          <span className="text-sm text-muted-foreground">#{ticket.id}</span>
        </div>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-2">
          <div>
            <div className="text-sm text-muted-foreground">From</div>
            <div className="font-semibold capitalize">{from}</div>
          </div>
          <div>
            <div className="text-sm text-muted-foreground">To</div>
            <div className="font-semibold capitalize">{to}</div>
          </div>
          <div className="flex items-center gap-2">
            <Calendar className="h-4 w-4" />
            <span>{new Date().toLocaleDateString()}</span>
          </div>
        </div>
        <div className="text-sm text-muted-foreground">Transport: {ticket.transportType}</div>
      </CardContent>
    </Card>
  );
}

```


# File: pages\UserLogin.page.tsx

```tsx
import React, { useState } from "react";

interface UserData {
  username: string;
  password: string;
}

const UserLogin: React.FC = () => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [message, setMessage] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const userData: UserData = {
      username,
      password,
    };

    try {
      const API_URL = import.meta.env.VITE_BACK_END_URL;
      const response = await fetch(`${API_URL}/user/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      });

      console.log("Response:", response);

      if (response.ok) {
        response.json().then((data) => {
          console.log("Login successful:", data);
            localStorage.setItem("Authorization", data.token);

            window.location.href = "/"; 
        }
        );
        setMessage("Login successful!");
      } else {
        setMessage("Failed to login.");
        console.error("Failed to login:", response.statusText);
      }
    } catch (error) {
      setMessage("Error during login.");
      console.error("Error during login:", error);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="w-96 p-6 bg-white rounded-lg shadow-lg">
        <h2 className="text-2xl font-bold text-center text-gray-700 mb-6">Login to Public Transport Tickets</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-600 font-medium" htmlFor="userName">
              Username
            </label>
            <input
              type="text"
              id="userName"
              name="userName"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full px-4 py-2 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your username"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-600 font-medium" htmlFor="password">
              Password
            </label>
            <input
              type="password"
              id="password"
              name="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-2 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your password"
              required
            />
          </div>
          {message && (
            <div
              className={`mt-4 p-3 rounded-md text-center ${
                message.includes("Error") || message.includes("Failed") ? "bg-red-100 text-red-600" : "bg-green-100 text-green-600"
              }`}
            >
              {message}
            </div>
          )}
          <button
            type="submit"
            className="w-full mt-6 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default UserLogin;

```


# File: pages\UserRegister.page.tsx

```tsx
import React, { useState } from "react";

interface UserData {
  userName: string;
  email: string;
  password: string;
}

const UserRegister: React.FC = () => {
  const [userName, setUserName] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [message, setMessage] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const userData: UserData = {
      userName,
      email,
      password,
    };

    try {
      const API_URL = import.meta.env.VITE_BACK_END_URL;
      const response = await fetch(`${API_URL}/user/register`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      });

      console.log("Response:", response);

      if (response.status === 201) {
        setMessage("User registered successfully!");
        window.location.href = "/login"; 
      } else {
        setMessage("Failed to register user.");
        console.error("Failed to register user:", response.statusText);
      }
    } catch (error) {
      setMessage("Error during registration.");
      console.error("Error during registration:", error);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="w-96 p-6 bg-white rounded-lg shadow-lg">
        <h2 className="text-2xl font-bold text-center text-gray-700 mb-6">Register for Public Transport Tickets</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-600 font-medium" htmlFor="userName">
              Full Name
            </label>
            <input
              type="text"
              id="userName"
              name="userName"
              value={userName}
              onChange={(e) => setUserName(e.target.value)}
              className="w-full px-4 py-2 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your full name"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-600 font-medium" htmlFor="email">
              Email Address
            </label>
            <input
              type="email"
              id="email"
              name="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-4 py-2 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your email"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-600 font-medium" htmlFor="password">
              Password
            </label>
            <input
              type="password"
              id="password"
              name="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-2 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your password"
              required
            />
          </div>
          {message && (
            <div
              className={`mt-4 p-3 rounded-md text-center ${
                message.includes("Error") || message.includes("Failed") ? "bg-red-100 text-red-600" : "bg-green-100 text-green-600"
              }`}
            >
              {message}
            </div>
          )}
          <button
            type="submit"
            className="w-full mt-6 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            Register
          </button>
        </form>
      </div>
    </div>
  );
};

export default UserRegister;

```


# File: utils\Router.tsx

```tsx
import { createBrowserRouter } from "react-router-dom"
import RootLayout from "@/pages/layout"
import HomePage from "@/pages/Home.pages"
import UserRegister from "@/pages/UserRegister.page"
import UserLogin from "@/pages/UserLogin.page"
import MyTicketsPage from "@/pages/Ticket"
import RouteSearchPage from "@/pages/Search.pages"

export const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    children: [
      {
        index: true,
        element: <HomePage />,
      },
      {
        path: "register",
        element: <UserRegister />,
      },
      {
        path: "login",
        element: <UserLogin />,
      },
      {
        path: "my-tickets",
        element: <MyTicketsPage />,
      },
      {
        path: "routes/search",
        element: <RouteSearchPage />,
      }
    ],
  },
])

```


# File: vite-env.d.ts

```ts
/// <reference types="vite/client" />

```

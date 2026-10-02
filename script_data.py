"""Single source of truth for the v5 speaking script.
build.py turns this into the Word doc and the practice app's default content.
kind: "say" = words out loud, "do" = an action / cue (pause, broadcast, etc.)
"""

SLIDES = [
    {
        "title": "The Shift: Compliance vs. Cooperation",
        "time": "~1:00",
        "chunks": [
            ("The contrast", "say", "Look at the contrast on this slide. In a traditional hierarchy, managers rely on positional power: do this because I'm the boss. Even when it works, the result is reluctant compliance. People do just enough not to get in trouble."),
            ("Who you actually need", "say", "Now think about who you actually need help from: engineering, finance, legal, other departments. If you try to tell your peers what to do, you might hear something along the lines of: \"You're not the boss of me.\""),
            ("What we want (right side)", "say", "What we really want is on the right: willing commitment, where people bring real effort because they want the project to succeed."),
            ("Carnegie quote", "say", "As Dale Carnegie put it: \"First, arouse in the other person an eager want.\""),
            ("Transition", "say", "How do we do that? It starts with the foundation of influence, but first, what gets in our way?"),
        ],
    },
    {
        "title": "What gets in the way",
        "time": "~0:30",
        "chunks": [
            ("Frame the slide", "say", "The course starts by naming what gets in the way. These are ten common obstacles from the course."),
            ("The ask", "say", "Take ten seconds and silently pick the one you've felt most recently."),
            ("Pause", "do", "[PAUSE ~8 seconds]"),
            ("Optional chat cue", "do", "[Facilitator cue: Optional: invite one or two people to type their number in chat.]"),
        ],
    },
    {
        "title": "The Influence Triad",
        "time": "~1:00",
        "chunks": [
            ("Intro", "say", "Dale Carnegie teaches that influence rests on three interdependent legs: Trust, Credibility, and Respect."),
            ("Trust", "say", "Trust is about reliability: can I count on you to do what you said you would?"),
            ("Credibility", "say", "Credibility is about expertise: have you earned the right to ask? Have you done your homework, or are you bringing half-baked asks?"),
            ("Respect", "say", "Respect is about recognizing what the other person brings: their abilities, their work, their team's contribution. Do you value it, or do you treat them like a service?"),
            ("Interdependence", "say", "The three depend on each other. If any single leg is broken, influence collapses."),
        ],
    },
    {
        "title": "Map who you need to influence",
        "time": "~0:45",
        "chunks": [
            ("Step one: who", "say", "Step one is getting intentional about who. The Personal Influence Chart puts you in the middle and maps the people around you: your boss and your boss's peers, other leaders, other teams, your peers and their teams, and your own team."),
            ("The course's point", "say", "The course makes a simple point: we are already influencing everyone we interact with, but we're often not aware of it. When we become intentional about it, relationships get stronger and cooperation goes up."),
            ("The question", "say", "Who is the one person on this map you'd most like more influence with? Hold onto that person. You'll use it in the breakout."),
        ],
    },
    {
        "title": "The 6 Questions to Get Results",
        "time": "~1:30",
        "chunks": [
            ("Set up the approach", "say", "Here is the six-question approach from the course for making a respectful request."),
            ("The usual ask", "say", "Usually, when we ask a peer for help, what do we say? \"Hey, are you free? I really need you to pull this data for my deck tomorrow.\" That's not a strategic request; it's an intrusion, and it ignores their priorities."),
            ("Questions 1-3", "say", "One through three explain the need: the situation, the specific result, and why it matters."),
            ("Question 6", "say", "Six closes the loop with a clear agreement on expectations, timing and follow-up."),
            ("Where we'll focus", "say", "A lot of times people will skip four and five, so that's where we'll focus today."),
            ("Question 4: Impact", "say", "Question four is the impact if it doesn't get done. It's about clarity, not threats. \"Without your data, we could lose the contract.\" That grounds the deadline in business reality."),
            ("Question 5: WIIFM", "say", "Question five is what's in it for them. If you approach a peer as a supplicant asking for charity, you go to the bottom of their backlog. If you show how this helps them, such as \"we use your real numbers to justify your department's staffing and protect your budget,\" you move up the list."),
            ("Closing line", "say", "Don't ask for favors. Build strategic partnerships."),
        ],
    },
    {
        "title": "Same request, two ways",
        "time": "~0:45",
        "chunks": [
            ("Set the scene", "say", "Here's an example of what this looks like: I need maintenance and overtime numbers from a colleague in another department, because regional leadership is reviewing budgets and headcount on Friday."),
            ("Left side: the usual ask", "say", "On the left is the ask a lot of us would make: \"Can you get your budget numbers in?\""),
            ("Right side: same ask, six questions", "say", "On the right is the same ask using the six questions. It's still only about thirty seconds of talking."),
            ("1. Situation", "say", "It names the situation: leadership is reviewing budgets and headcount Friday."),
            ("2. Result", "say", "It states the specific result: finalized maintenance and overtime numbers by Wednesday at noon."),
            ("3. Why", "say", "It gives the reason: leadership allocates contractor support and Capex from this data."),
            ("4. Impact", "say", "Then the impact: without it, their team's workload is invisible and vulnerable to budget cuts."),
            ("5. Mutual benefit", "say", "Then what's in it for them: we use their real numbers to justify their staffing and protect their budget."),
            ("6. Agreement", "say", "It closes with a clear agreement: I'll confirm by email, and we do a five-minute sync Thursday morning."),
            ("The payoff", "say", "The other person can say yes, or negotiate, but either way they know exactly what they're deciding."),
        ],
    },
    {
        "title": "The Cross-Functional Pitch Challenge",
        "time": "~0:15 to frame, then 4:00 in breakouts",
        "chunks": [
            ("Set up the pairs", "say", "We're going into pairs for exactly four minutes. Pick someone you need results from."),
            ("Person A", "say", "In about 90 seconds, Person A pitches the ask. Focus on question four, the impact if it isn't done, and question five, what's in it for them. Keep it to about a minute so your partner has time for a quick comment."),
            ("The swap", "say", "At the two-and-a-half-minute chat, swap and Person B pitches."),
            ("Last minute", "say", "In the last minute, discuss and prepare one insight."),
            ("Open the rooms", "say", "Let's open the rooms."),
            ("Broadcast at 2:30", "do", "Broadcast at 2:30: \"Halfway mark! Swap roles now.\""),
            ("Broadcast at 4:00", "do", "Broadcast at 4:00: \"1 minute left. Capture one insight.\""),
            ("Close the rooms", "do", "Close rooms at 4:00."),
        ],
    },
    {
        "title": "Let's hear it (Debrief)",
        "time": "~1:30",
        "chunks": [
            ("Welcome back", "say", "Welcome back. Let's hear it. Does anyone have an insight they'd like to share from their breakout room? If you need ideas, here are a few questions you can answer."),
            ("Question 1", "say", "Did it make you think differently about how you might approach this person?"),
            ("Question 2", "say", "What did you notice listening to someone else's ask? Was it clear what they wanted?"),
            ("Question 3", "say", "What was the hardest question to answer and why?"),
            ("What I'm hearing", "say", "What I'm hearing is that the hard part usually isn't the tool. It's slowing down enough to be specific and to see the request from the other person's side."),
            ("Carnegie principle 17", "say", "That's exactly what Carnegie's principle 17 is about: try honestly to see things from the other person's point of view."),
            ("If it's quiet", "do", "[Facilitator cue: If it's quiet, go first with your own answer or call on someone by name. Thank each speaker. Stop at about 90 seconds; invite people to keep talking afterward.]"),
        ],
    },
    {
        "title": "The Trap: Stop \"Buying It Back\"",
        "time": "~1:00",
        "chunks": [
            ("Intro", "say", "Lastly, I want to leave you with a few traps that I'm sure many of you have fallen into, myself included."),
            ("Trap 1: Buy it back", "say", "When a peer hesitates, our instinct is to say, \"You know what, leave it with me, I'll finish the draft.\" That's called buying it back. You think you're being helpful, but the assignment stays with you, and nothing moves until you do something. You've become the bottleneck."),
            ("Trap 2: Put in limbo", "say", "The second trap is putting it in limbo: \"If you have free time...\", \"Let's wait until the next meeting...\". The process slows and decisions get delayed. It dies in the backlog."),
            ("The fix", "say", "Instead, establish accountability, and make it clear the ownership has shifted: \"You're the right person for the job. What's your plan for hitting the Friday milestone? I'm counting on your leadership.\""),
            ("Result", "say", "Results are much more likely."),
        ],
    },
    {
        "title": "Thank you",
        "time": "~0:15",
        "chunks": [
            ("Thank you + resources", "say", "Thank you. If you've taken the course, the job aids and Mastery Moments videos in your Dale Carnegie learning portal are a good refresher."),
            ("Q&A offer", "say", "I'm happy to take a question or two, or catch anyone afterward."),
            ("Stop sharing", "do", "[Facilitator cue: Stop sharing or leave this slide up for Q&A.]"),
        ],
    },
]

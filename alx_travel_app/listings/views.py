# listings/views.py

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, editing, and managing Listings.
    Provides CRUD operations.
    """
    queryset = Listing.objects.all().order_by('-created_at')
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Allow filtering by location
        queryset = Listing.objects.all().order_by('-created_at')
        location = self.request.query_params.get('location', None)
        if location:
            queryset = queryset.filter(location__icontains=location)
        return queryset.prefetch_related('amenities').annotate(
            average_rating=models.Avg('reviews__rating'),
            reviews_count=models.Count('reviews')
        )

    @action(detail=True, methods=['get'], url_path='bookings')
    def bookings(self, request, pk=None):
        """Get all bookings for a specific listing"""
        listing = self.get_object()
        bookings = listing.bookings.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


class BookingViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and managing Bookings.
    Users can only manage their own bookings.
    """
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Booking.objects.filter(guest=user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(guest=self.request.user)